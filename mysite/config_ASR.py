#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser


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
            '380688846025@sms.kyivstar.net',
        ],
    "Boston":
        [
            '20flint12@gmail.com',
            # '380688845064@sms.kyivstar.net',
        ],
}




EMAIL_SENDER   = "astroreminder@gmail.com"
EMAIL_USERNAME = "astroreminder@gmail.com"
EMAIL_PASSWORD = "95dd2d30 "






def write_geo_to_config():

    config = ConfigParser.RawConfigParser()

    # # When adding sections or items, add them in the reverse order of
    # # how you want them to be displayed in the actual file.
    # # In addition, please note that using RawConfigParser's and the raw
    # # mode of ConfigParser's respective set functions, you can assign
    # # non-string values to keys internally, but will receive an error
    # # when attempting to write to a file or when you get it in non-raw
    # # mode. SafeConfigParser does not allow such assignments to take place.
    # config.add_section('Section')
    # config.set('Section', 'an_int', '15')
    # config.set('Section', 'a_bool', 'true')
    # config.set('Section', 'a_float', '3.1415')
    # config.set('Section', 'baz', 'fun')
    # config.set('Section', 'bar', 'Python')
    # config.set('Section', 'foo', '%(bar)s is %(baz)s!')


    config.add_section('USART device:')
    config.set('USART device:', 'name', config_MAG.SERIAL_DEV)

    config.add_section('Files:')
    config.set('Files:', 'input  (*.txt)', config_MAG.FILE_TXT)
    config.set('Files:', 'Output directory', config_MAG.SAVE_TO_DIR)
    config.set('Files:', 'Output file name', config_MAG.CSV_NAME)

    config.add_section('Gateway:')
    config.set('Gateway:', 'IP address', config_MAG.SERVER)


    # Writing our configuration file to 'settings.cfg'
    with open('settings.cfg', 'wb') as configfile:
        config.write(configfile)
        print "Configuration saved."





def read_config_to_geo():

    try:

        with open('settings.cfg', 'r') as configfile:

            config = ConfigParser.RawConfigParser()

            config.readfp(configfile)

            # # print config._sections
            # # getfloat() raises an exception if the value is not a float
            # # getint() and getboolean() also do this for their respective types
            # a_float = config.getfloat('Section', 'a_float')
            # an_int = config.getint('Section', 'an_int')
            # print a_float + an_int
            #
            # # Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
            # # This is because we are using a RawConfigParser().
            # if config.getboolean('Section', 'a_bool'):
            #     print config.get('Section', 'foo')

            print "\n   Reading config file..."

            config_MAG.SERIAL_DEV  = config.get('USART device:', 'name')
            config_MAG.FILE_TXT    = config.get('Files:', 'input  (*.txt)')
            config_MAG.SAVE_TO_DIR = config.get('Files:', 'Output directory')
            config_MAG.CSV_NAME    = config.get('Files:', 'Output file name')
            config_MAG.SERVER      = config.get('Gateway:', 'IP address')

            print 'Serial ports is:', config_MAG.SERIAL_DEV
            print 'Input file is  :', config_MAG.FILE_TXT
            print 'Output file is :', config_MAG.SAVE_TO_DIR + config_MAG.CSV_NAME
            print 'Server IP is   :', config_MAG.SERVER



    except IOError:

        print "there is no config file!!!"
        print "used defaults..."
