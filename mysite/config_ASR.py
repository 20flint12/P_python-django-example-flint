#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
# linux hostname

HOSTNAME = os.uname()[1]


# Load defaults ---------------------------------------------------------------

# Server name
SERVER_NAME = 'Unknown server'
# Server ip
SERVER_IP = 'localhost'
# Mail to addresses
EMAIL_LIST = ["20flint12@gmail.com"]


print "HOSTNAME   :", HOSTNAME
# print "SERVER_NAME:", SERVER_NAME
# print "SERVER_IP  :", SERVER_IP

#------------------------------------------------------------------------------



GEO_PLACE = {

    "Kharkiv":
        {"time_zone": 2,
         "location": [50.0, 36.15]},
    "Kremenchug":
        {"time_zone": 2,
         "location": [22,50]},
    "Boston":
        {"time_zone": -4,
         "location": [22,50]},
}


EMAIL_SET = {

    "Kharkiv":
        [
            '20flint12@gmail.com',
            '380688845064@sms.kyivstar.net',
        ],
    "Kremenchug":
        [
            '20flint12@gmail.com',
            '380688845064@sms.kyivstar.net',
        ],
    "Boston":
        [
            '380688845064@sms.kyivstar.net',
        ],
}




EMAIL_SENDER   = "astroreminder@gmail.com"
EMAIL_USERNAME = "astroreminder@gmail.com"
EMAIL_PASSWORD = "95dd2d30 "



