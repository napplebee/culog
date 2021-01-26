#!/usr/bin/env python

from bin.data import db
from bin.data.blog_post import BlogPost
from configs import Config as cfg
from app.common.constants import Constants as cnst
import requests as r
import traceback
import json
import os


def get_token():
    client_id = os.environ.get('FB_CLIENT_ID')
    client_secret = os.environ.get('FB_CLIENT_SECRET')
    payload = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
    file = r.post('https://graph.facebook.com/oauth/access_token?', params=payload)
    return file.json()['access_token']
    # return file.text.split("=")[1]


def run():
    token = get_token()

    report = []
    posts = db.query(BlogPost).filter(BlogPost.visible and BlogPost.url != "").all()
    for post in posts:
        log = {}
        log["post_id"] = post.id
        log["old_shares"] = post.fb_likes
        total_shares = 0
        try:
            for lng in cnst.SUPPORTED_LANGS:
                url = "{0}/{1}/{2}".format(cfg.BASE_EXTERNAL_URI, lng, post.url)
                fb_request_url = "https://graph.facebook.com/v2.8/?id={0}&access_token={1}".format(url, token)
                response = r.get(fb_request_url)
                log[lng] = response.status_code
                if response.status_code != r.codes.ok:
                    continue
                    # todo: logging
                data = response.json()
                if "share" in data and "share_count" in data["share"]:
                    shares = int(data["share"]["share_count"])
                    total_shares += shares
                    log[lng+"_new_shares"] = shares
                else:
                    log[lng+"_new_shares"] = 0
        except Exception as e:
            log["exception"] = traceback.format_exc()
        
        post.fb_likes = total_shares
        report.append(log)

    # send_report(json.dumps(report, indent=3, sort_keys=True))
    print(report)
    db.commit()


def send_report(report):
    import sendgrid

    sg_user = os.environ.get('SENDGRID_USER')
    sg_pwd = os.environ.get('SENDGRID_PWD')
    sg = sendgrid.SendGridClient(sg_user, sg_pwd)

    message = sendgrid.Mail()
    message.add_to('belikov.sergey@gmail.com')
    message.set_subject('FB shares report')
    message.set_text(report)
    message.set_from('info@cookwith.love')
    sg.send(message)

run()
