#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from django.core.mail import send_mail

import ephem
import astro_routines.moon_day as md

import pprint




def my_email(str_data):

    # send_mail('Subject here',
    #           'Here is the message.',
    #           'astroreminder@gmail.com',
    #           ['20flint12@gmail.com'],
    #           fail_silently=False)

    try:
        send_mail('Info',
                   str_data,
                  'astroreminder@gmail.com',
                  ['20flint12@gmail.com','380688845064@sms.kyivstar.net'],
                  fail_silently=False)
    except:
        str_res = "Unexpected error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        print str_res
        # sys.exit()





def email_reminder():

    cur_date_utc = ephem.now()  # current UTC date and time
    tp, ctx2, cur_mday = md.get_phase_on_current_day(cur_date_utc)

    print "tp=", pprint.pprint(tp)
    # tp={'day_rise': 42324.914049849416,
    # 'day_sett': 42325.34484464035,
    # 'moon_day': 8,
    # 'new_rise': 42325.93734154524,
    # 'str_day_rise': 'UTC:2015/11/18 09:56:14 {2015-11-18 11:56:13}',
    # 'str_day_sett': 'UTC:2015/11/18 20:16:35 {2015-11-18 22:16:34}',
    # 'str_new_rise': 'UTC:2015/11/19 10:29:46 {2015-11-19 12:29:46}'}
    str_msg = str(tp["moon_day"]) + " moon day: " + \
              tp["str_day_rise"] + " " + \
              tp["str_day_sett"] + " " + \
              tp["str_new_rise"]
    print str_msg, " ||| ", len(str_msg)

    # print EMAIL_HOST
    print "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ"
    my_email(str_msg)
    # my_mail2("Reminder", "test1", "test2")





###############################################################################


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mysite.config_ASR as conf


def send_mail2(mail_subject, str_plain, str_html):

    for email in conf.EMAIL_LIST:

        fromaddr = conf.EMAIL_SENDER
        toaddrs  = email


        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = mail_subject
        msg['From']    = fromaddr
        msg['To']      = toaddrs


        # Create the body of the message (a plain-text and an HTML version).
        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
        text = str_plain
        html = str_html

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        # Send the message via local SMTP server XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # server = smtplib.SMTP('localhost')
        # # sendmail function takes 3 arguments: sender's address, recipient's address
        # # and message to send - here it is sent as one string.
        # server.sendmail(fromaddr, toaddr, msg.as_string())
        # server.quit()

        # ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        # Send the message via google SMTP server XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        # Credentials (if needed)
        username = conf.EMAIL_USERNAME
        password = conf.EMAIL_PASSWORD

        # The actual mail send
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()

        print "\n### mail to {:s} sent.".format(email)






if __name__ == '__main__':

    email_reminder()




