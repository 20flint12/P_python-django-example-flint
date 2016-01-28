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


GEO_FILE = "geo_data.cfg"




EMAIL_SET = {

    "Kharkiv":
        [
            # '20flint12@gmail.com',
            '380688845064@sms.kyivstar.net',
            #-------------------------------
            '380688846025@sms.kyivstar.net',    # Инна
            '380975135252@sms.kyivstar.net',    # Володя-планетарий
            '380973497865@sms.kyivstar.net',    # Юра-планетарий

        ],
    "Kremenchug":
        [
            '20flint12@gmail.com',
            #-------------------------------
            '380678986620@sms.kyivstar.net',    # мама
            '380681546330@sms.kyivstar.net',    # тёща
        ],
    "Boston":
        [
            '20flint12@gmail.com',
            # '380688845064@sms.kyivstar.net',
        ],
    "Moscow":
        [
            '20flint12@gmail.com',
            # '380688845064@sms.kyivstar.net',
        ],
    "London":
        [
            '20flint12@gmail.com',
            # '380688845064@sms.kyivstar.net',
        ],
}




EMAIL_SENDER   = "astroreminder@gmail.com"
EMAIL_USERNAME = "astroreminder@gmail.com"
EMAIL_PASSWORD = "95dd2d30 "





