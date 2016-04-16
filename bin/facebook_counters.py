#!/usr/bin/env python
from bin.data import db
from bin.data.blog_post import BlogPost
from configs import Config as cfg
import requests as r
import os
import traceback


def run():
    report = ""
    posts = db.query(BlogPost).filter(BlogPost.visible and BlogPost.url != "").all()
    for post in posts:
        report += "post_id: {0}, old_shares: {1}, ".format(post.id, post.fb_likes)
        total_shares = 0
        try:
            for lng in cfg.SUPPORTED_LANGS:
                url = "{0}/{1}/{2}".format(cfg.BASE_EXTERNAL_URI, lng, post.url)
                response = r.get("http://graph.facebook.com/?id={0}".format(url))
                report += "{0}:req_status: {1}, ".format(lng, response.status_code)
                if response.status_code != r.codes.ok:
                    continue
                    # todo: logging
                data = response.json()
                if "shares" in data:
                    shares = int(data["shares"])
                    total_shares += shares
                    report += "new_shares: {0}, ".format(shares)
                else:
                    report += "new_shares: 0, "
        except Exception as e:
            report += "Exception occured: {0}".format(traceback.format_exc())

        if total_shares > 0:
            post.fb_likes = total_shares

        report += os.linesep
    print
    send_report(report)
    db.commit()


def send_report(report):
    import sendgrid

    sg = sendgrid.SendGridClient('culog_mailer', 'jx3ymlkbyysqgfhjkm')

    message = sendgrid.Mail()
    message.add_to('belikov.sergey@gmail.com')
    message.set_subject('FB shares report')
    message.set_text(report)
    message.set_from('info@cookwith.love')
    sg.send(message)

run()