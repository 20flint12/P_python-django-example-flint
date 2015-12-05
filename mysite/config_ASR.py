#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser
import pprint

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






def write_geo_to_config(path_to_file, in_place_dict):

    config = ConfigParser.RawConfigParser()

    for place in in_place_dict.keys():

        coord = in_place_dict[place]["coord"]
        dst = in_place_dict[place]["dst"]
        print place, coord, dst, "-"*40

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

        config.add_section(place)
        config.set(place, 'coord', coord)
        config.set(place, 'dst', dst)

    # Writing our configuration file to 'settings.cfg'
    with open(path_to_file, 'wb') as configfile:
        config.write(configfile)
        print "Configuration saved."



def as_dict(config):
    """
    Converts a ConfigParser object into a dictionary.

    The resulting dictionary has sections as keys which point to a dict of the
    sections options as key => value pairs.
    """
    the_dict = {}
    for section in config.sections():
        the_dict[section] = {}
        for key, val in config.items(section):
            the_dict[section][key] = val
    return the_dict



def read_config_to_geo(path_to_file):

    try:

        with open(path_to_file, 'r') as configfile:

            config = ConfigParser.RawConfigParser()

            config.readfp(configfile)

            # # # print config._sections
            # # # getfloat() raises an exception if the value is not a float
            # # # getint() and getboolean() also do this for their respective types
            # # a_float = config.getfloat('Section', 'a_float')
            # # an_int = config.getint('Section', 'an_int')
            # # print a_float + an_int
            # #
            # # # Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
            # # # This is because we are using a RawConfigParser().
            # # if config.getboolean('Section', 'a_bool'):
            # #     print config.get('Section', 'foo')
            #
            # print "\n   Reading config file..."

            res_dict = as_dict(config)

            # print "res_dict=", res_dict
            return res_dict


    except IOError:

        print "there is no config file!!!"
        print "used defaults..."




GEO_PLACE_dict= \
    {
        'Kremtotqwe':
            {
                'dst': 'False',
                'coord': (1221, 78)
            },
        'Kharkov':
            {
                'dst': 'Fals4444e',
                'coord': (1222, 79)
            },
        'BBBBBBost':
            {
                'dst': 'True',
                'coord': '(1223, 78)'
            },
    }



if __name__ == '__main__':

    path_to_file = 'settings.cfg'

    # place = "Kremtotqwe"
    # coord = (1221, 78)
    # dst   = False
    #
    # write_geo_to_config(place, coord, dst)

    write_geo_to_config(path_to_file, GEO_PLACE_dict)


    out_place_dict = read_config_to_geo(path_to_file)
    print "out_place_dict=\n", pprint.pprint(out_place_dict)