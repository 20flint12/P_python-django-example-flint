
import sys
import pprint
from datetime import *

from django.core.mail import send_mail


import reminder.config_ASR as conf
import engine.astro_routines.moon_day as md

import engine.astro_routines.geo_place as geo
import engine.astro_routines.sun_rise_sett as srs
import engine.astro_routines.zodiac_phase as zod

import grabber.scrapes.scrape_solar_activity as sa


def my_email(str_subject, str_body, list_emails):

    try:
        send_mail(str_subject, str_body,
                  'astroreminder@gmail.com',
                  list_emails,  # ['20flint12@gmail.com','380688845064@sms.kyivstar.net'],
                  fail_silently=False)
    except:
        str_res = "Unexpected error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
        print(str_res)
        # sys.exit()


def email_reminder():

    for cur_place in conf.EMAIL_SET.keys():

        list_emails = conf.EMAIL_SET[cur_place]
        print("list_emails=", list_emails)

        cur_date_loc = datetime.today() ### server time

        cur12_aware_loc, cur12_unaware_utc = \
            geo.aware_loc_unaware_utc_for_local12place(cur_date_loc, cur_place)
        # print "cur12_aware_loc, cur12_unaware_utc =", cur12_aware_loc, cur12_unaware_utc


        # str_on = aware_loc.strftime("%d %b %H:%M%z")[:-2]
        # str_on = tp_md_ext["aware_loc"].strftime("%d %b %H:%M%z")[:-2]
        str_on = cur12_aware_loc.strftime("%d %b %H:%M%z")[:-2]
        # print "str_on=", str_on

        format  = "%d %b %H:%M"
        format2 = "%H:%M"

        out_str_msg = u""
        # *********************************************************************


        # out_str_subject = str_on + " " + cur_place
        out_str_subject = cur_place + " " + str_on
        print("out_str_subject=", out_str_subject)
        # out_str_msg += out_str_subject + "\n"
        # ----------------------------------------------------------------------

        tp_srs_ext = srs.get_sun_rise_sett_local12place(cur_date_loc, cur_place)
        # print "tp_srs_ext=", pprint.pprint(tp_srs_ext)
        # =====================================================================
        out_str_msg += u"\n### Солнце ###\n"
        out_str_msg += u"восход " + tp_srs_ext["day_rise_loc"].strftime(format2) + "\n"
        out_str_msg += u"закат  " + tp_srs_ext["day_sett_loc"].strftime(format2) + "\n"
        # ----------------------------------------------------------------------

        td = timedelta(hours=12)
        # ecl_dict_ext = zod.get_zodiac_local12place(cur12_aware_loc-td, cur12_unaware_utc-td, "Sun", cur_place)
        # out_str_msg += ecl_dict_ext["zod_lat"] + "-"
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ecl_dict_ext = zod.get_zodiac_local12place(cur12_aware_loc, cur12_unaware_utc,
                                                   "Sun", cur_place)
        # print "ecl_dict_ext=", pprint.pprint(ecl_dict_ext)
        # =====================================================================
        # out_str_msg += "Sun:\n"
        # out_str_msg += str(ecl_dict_ext["ecl.lon"]) + "\n"
        out_str_msg += ecl_dict_ext["zod_lat"] + "\n"
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ecl_dict_ext = zod.get_zodiac_local12place(cur12_aware_loc+td, cur12_unaware_utc+td, "Sun", cur_place)
        # out_str_msg += ecl_dict_ext["zod_lat"] + "\n"
        # ----------------------------------------------------------------------

        solar_lst = sa.get_solar_activity()
        print("solar_lst=", pprint.pprint(solar_lst))
        # =====================================================================
        # out_str_msg += "\n"
        out_str_msg += solar_lst[0][0] + ": "   # ACTIVE
        out_str_msg += solar_lst[0][1] + "-"
        out_str_msg += solar_lst[0][2] + "%\n"

        # out_str_msg += solar_lst[1][0] + ": "   # MINOR
        # out_str_msg += solar_lst[1][1] + "-"
        # out_str_msg += solar_lst[1][2] + "%\n"

        out_str_msg += solar_lst[2][0] + ": "   # SEVERE
        out_str_msg += solar_lst[2][1] + "-"
        out_str_msg += solar_lst[2][2] + "%\n"

        tp_md_ext = md.get_moon_day_ext(cur12_aware_loc, cur12_unaware_utc, cur_place)
        # print "tp_md_ext=\n", pprint.pprint(tp_md_ext)
        # =====================================================================
        out_str_msg += u"\n### Луна ###\n"
        out_str_msg += unicode(tp_md_ext["moon_day"]) + u" лунный день\n"
        out_str_msg += u"восход  " + tp_md_ext["day_rise_loc"].strftime(format) + "\n"
        out_str_msg += u"заход   " + tp_md_ext["day_sett_loc"].strftime(format) + "\n"
        out_str_msg += u"сл.восх " + tp_md_ext["new_rise_loc"].strftime(format) + "\n"
        # ---------------------------------------------------------------------

        ecl_dict_ext = zod.get_zodiac_local12place(cur12_aware_loc-td, cur12_unaware_utc-td, "Moon", cur_place)
        out_str_msg += ecl_dict_ext["zod_lat"] + "-"
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ecl_dict_ext = zod.get_zodiac_local12place(cur12_aware_loc, cur12_unaware_utc,
                                                   "Moon", cur_place)
        # print "ecl_dict_ext=", pprint.pprint(ecl_dict_ext)
        # =====================================================================
        # out_str_msg += "\n"
        # out_str_msg += str(ecl_dict_ext["ecl.lon"]) + "\n"
        out_str_msg += ecl_dict_ext["zod_lat"] + "-"
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ecl_dict_ext = zod.get_zodiac_local12place(cur12_aware_loc+td, cur12_unaware_utc+td, "Moon", cur_place)
        out_str_msg += ecl_dict_ext["zod_lat"] + "\n"
        # ---------------------------------------------------------------------

        tp_mph_ext = md.get_moon_phase_local12place(cur_date_loc, cur_place)
        # print "tp_mph_ext=", pprint.pprint(tp_mph_ext)
        # =====================================================================
        # out_str_msg += "\n"
        prev_phase = tp_mph_ext["prev"] + "_loc"
        next_phase = tp_mph_ext["next"] + "_loc"

        prev_mom = tp_mph_ext["prev"][-2:]
        next_mom = tp_mph_ext["next"][-2:]

        out_str_msg += u"пред: "
        if prev_mom == "NM":
            out_str_msg += u"новолуние"
        elif prev_mom == "FQ":
            out_str_msg += u"перв.четв"
        elif prev_mom == "FM":
            out_str_msg += u"полная л."
        elif prev_mom == "LQ":
            out_str_msg += u"трет.четв"
        out_str_msg += " " + tp_mph_ext[prev_phase].strftime(format) + "\n"

        out_str_msg += u"след: "
        if next_mom == "NM":
            out_str_msg += u"новолуние"
        elif next_mom == "FQ":
            out_str_msg += u"перв.четв"
        elif next_mom == "FM":
            out_str_msg += u"полная л."
        elif next_mom == "LQ":
            out_str_msg += u"трет.четв"
        out_str_msg += " " + tp_mph_ext[next_phase].strftime(format) + "\n"
        # ---------------------------------------------------------------------


        # ### Солнце ###
        # восход 07:29
        # закат  15:58
        # 22Коз
        # ACTIVE: 10-10%
        # MINOR_: 01-01%
        # SEVERE: 01-01%
        #
        # ### Луна ###
        # 5 лунный день
        # восход  13 Jan 09:09
        # заход   13 Jan 20:20
        # сл.восх 14 Jan 09:40
        # пред. новолуние 10 Jan 03:30
        # след. перв.четв 17 Jan 01:26
        # 28Вод-05Рыб-13Рыб
        # Вод28-Рыб05-Рыб13


        # =====================================================================
        # print "out_str_msg=", out_str_msg, " |||"*5, len(out_str_msg)

        my_email(out_str_subject, out_str_msg, list_emails)
        #end_mail2("Reminder", "test1", "test2")
        print("Q"*80)


###############################################################################
###############################################################################
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

        print("\n### mail to {:s} sent.".format(email))


if __name__ == '__main__':

    email_reminder()















