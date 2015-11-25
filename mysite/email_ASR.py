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

        tz_name, coord = md.set_tz(cur_place)
        print "cur_place=", cur_place, coord, tz_name


        # # Calculate utc date on local noon for selected place ###############
        format = "%Y-%m-%d %H:%M:%S %z"
        ###########################################################################
        cur_date_loc = datetime.today()
        print "cur_date_loc=", cur_date_loc.strftime(format)

        # Calculate utc date on local noon for selected place #####################
        cur_noon_loc = datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
        print "cur_noon_loc=", cur_noon_loc

        # -------------------------------------------------------------------------
        aware_loc = geo.set_tz_to_unaware_time(tz_name, cur_noon_loc)
        print "aware_loc=", aware_loc.strftime(format)
        cur_date_utc = geo.aware_time_to_utc(aware_loc)
        print "cur_date_utc=", cur_date_utc.strftime(format), "utcoffset=", cur_date_utc.utcoffset()

        tp, ctx2 = md.get_phase_on_current_day(cur_date_utc, coord)
        print "tp=", pprint.pprint(tp)
        # tp={'day_rise': 42331.036574133206,
        # 'day_sett': 42331.58704307381,
        # 'moon_day': 14,
        # 'new_rise': 42332.072643126965,}

        str_on = aware_loc.strftime("%d %b %H:%M%z")[:-2]
        # print "str_on=", str_on


        # >>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        # 'Thu, 28 Jun 2001 14:17:15 +0000'
        # # time_stamp = today.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        format = "%d %b %H:%M"


        # Kremenchug on 25 Nov 12:00+02
        # 25 Nov 12:00+02 Kremenchug

        str_subject = str_on + " " + cur_place
        print "str_subject=", str_subject

        str_msg = str(tp["moon_day"]) + " moon day:\n"
        # str_msg += tp["str_day_rise"] + "\n"
        # str_msg += tp["str_day_sett"] + "\n"
        # str_msg += tp["str_new_rise"] + "\n"
        # print str_msg, " ||| ", len(str_msg)


        day_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp["day_rise"]).datetime())
        day_sett_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp["day_sett"]).datetime())
        new_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp["new_rise"]).datetime())

        str_msg += "rise " + str(day_rise_loc.strftime(format)) + "\n"
        str_msg += "sett " + str(day_sett_loc.strftime(format)) + "\n"
        str_msg += "next " + str(new_rise_loc.strftime(format)) + "\n"

        print str_msg, " |||"*5, len(str_msg)


        print "Q"*80
        my_email(str_subject, str_msg, list_emails)
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

    # cur_place = "Boston"
    # # cur_place = "Kharkiv"
    #
    # tz_name, coord = md.set_tz(cur_place)
    # print "cur_place=", cur_place, coord, tz_name
    #
    #
    # format = "%Y-%m-%d %H:%M:%S %z"
    # ###########################################################################
    # cur_date_loc = datetime.today()
    # print "cur_date_loc=", cur_date_loc.strftime(format)
    #
    # # Calculate utc date on local noon for selected place #####################
    # cur_noon_loc = datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
    # print "cur_noon_loc=", cur_noon_loc
    #
    # # -------------------------------------------------------------------------
    # # cur_date_utc = geo.loc_to_utc_time(tz_name, cur_noon_loc)
    # # print "cur_date_utc=", cur_date_utc.strftime(format), "utcoffset=", cur_date_utc.utcoffset()
    # #
    # # tp, ctx2 = md.get_phase_on_current_day(cur_date_utc, coord)
    # # print "tp=", pprint.pprint(tp)
    #
    # # -------------------------------------------------------------------------
    # aware_loc = geo.set_tz_to_unaware_time(tz_name, cur_noon_loc)
    # print "aware_loc=", aware_loc.strftime(format)
    # cur_date_utc = geo.aware_time_to_utc(aware_loc)
    # # print "aware_utc=",    cur_date_utc.strftime(format)
    # print "cur_date_utc=", cur_date_utc.strftime(format), "utcoffset=", cur_date_utc.utcoffset()
    #
    # tp, ctx2 = md.get_phase_on_current_day(cur_date_utc, coord)
    # print "tp=", pprint.pprint(tp)














