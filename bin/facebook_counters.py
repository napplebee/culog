#!/usr/bin/env python


def test():
    import sendgrid

    sg = sendgrid.SendGridClient('YOUR_SENDGRID_USERNAME', 'YOUR_SENDGRID_PASSWORD')

    message = sendgrid.Mail()
    message.add_to('belikov.sergey@gmail.com')
    message.set_subject('Example')
    message.set_text('Body')
    message.set_from('info@cookwith.love')
    status, msg = sg.send(message)



test()