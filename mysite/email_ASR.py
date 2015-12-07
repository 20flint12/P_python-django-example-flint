#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from django.core.mail import send_mail

import ephem
import astro_routines.moon_day as md

import pprint
from datetime import *

import mysite.config_ASR as conf
import mysite.astro_routines.geo_place as geo
import mysite.astro_routines.sun_rise_sett as srs

import mysite.astro_routines.geo_preload as geopr


def my_email(str_subject,str_body,list_emails):

    # send_mail('Subject here',
    #           'Here is the message.',
    #           'astroreminder@gmail.com',
    #           ['20flint12@gmail.com'],
    #           fail_silently=False)

    try:
        send_mail(str_subject, str_body,
                  'astroreminder@gmail.com',
                  list_emails, # ['20flint12@gmail.com','380688845064@sms.kyivstar.net'],
                  fail_silently=False)
    except:
        str_res = "Unexpected error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        print str_res
        # sys.exit()





def email_reminder():

    for cur_place in conf.EMAIL_SET.keys():

        list_emails = conf.EMAIL_SET[cur_place]
        print "list_emails=", list_emails

        tz_name, coord = geopr.set_tz(cur_place)
        # print "cur_place=", cur_place, coord, tz_name

        cur_date_loc = datetime.today()


        tp_md_ext = md.get_phase_on_local12_place(cur_date_loc, cur_place)
        # print "tp_md_ext=\n", pprint.pprint(tp_md_ext)
        # =====================================================================

        # str_on = aware_loc.strftime("%d %b %H:%M%z")[:-2]
        str_on = tp_md_ext["aware_loc"].strftime("%d %b %H:%M%z")[:-2]
        # print "str_on=", str_on

        # time_stamp = today.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        format = "%d %b %H:%M"

        # Kremenchug on 25 Nov 12:00+02
        # 25 Nov 12:00+02 Kremenchug

        str_subject = str_on + " " + cur_place
        print "str_subject=", str_subject

        str_msg = str(tp_md_ext["moon_day"]) + " moon day:\n"

        str_msg += "rise " + tp_md_ext["day_rise_loc"].strftime(format) + "\n"
        str_msg += "sett " + tp_md_ext["day_sett_loc"].strftime(format) + "\n"
        str_msg += "next " + tp_md_ext["new_rise_loc"].strftime(format) + "\n"
        #----------------------------------------------------------------------


        sd = srs.get_sun_rise_sett(tp_md_ext["date_utc"], coord)
        # print "sd=", pprint.pprint(sd)
        # =====================================================================

        str_msg += "sunrise - sunsett:\n"
        day_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(sd["day_rise"]).datetime())
        day_sett_loc = geo.utc_to_loc_time(tz_name, ephem.Date(sd["day_sett"]).datetime())

        str_msg += "rise " + str(day_rise_loc.strftime(format)) + "\n"
        str_msg += "sett " + str(day_sett_loc.strftime(format)) + "\n"
        #----------------------------------------------------------------------



        #======================================================================
        print str_msg, " |||"*5, len(str_msg)


        print "Q"*80
        # my_email(str_subject, str_msg, list_emails)
        # my_mail2("Reminder", "test1", "test2")





###############################################################################


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




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















