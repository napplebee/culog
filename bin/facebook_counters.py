#!/usr/bin/env python


def test():
    import sendgrid

    sg = sendgrid.SendGridClient('culog_mailer', 'jx3ymlkbyysqgfhjkm')

    message = sendgrid.Mail()
    message.add_to('belikov.sergey@gmail.com')
    message.set_subject('Example')
    message.set_text('Body')
    message.set_from('info@cookwith.love')
    status, msg = sg.send(message)



test()