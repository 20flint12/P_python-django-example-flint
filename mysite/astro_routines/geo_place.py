#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://stackoverflow.com/questions/16505501/get-timezone-from-city-in-python-django
# http://stackoverflow.com/questions/4563272/how-to-convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-stand


from datetime import datetime






def get_place_coord(in_place_name):

    from geopy import geocoders # pip install geopy

    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(in_place_name)     # Kremenchuk Boston

    # -> (u'Singapore', (1.352083, 103.819836))
    # print place, (lat, lng)
    return (lat, lng)



def get_tz_name(in_coord):

    from tzwhere import tzwhere

    w = tzwhere.tzwhere()

    tz_name = w.tzNameAt(in_coord[0], in_coord[1])

    # print "tz_name=", tz_name
    return tz_name



def set_tz_to_unaware_time(in_tz_name, in_unaware):

    import pytz

    local_tz = pytz.timezone(in_tz_name)  # 'Europe/Kiev'
    loc_aware = local_tz.localize(in_unaware)

    # print "loc_aware=", loc_aware
    return loc_aware

    # I had use from dt_aware to dt_unware
    #
    # dt_unaware = dt_aware.replace(tzinfo=None)
    #
    # and dt_unware to dt_aware
    #
    # from pytz import timezone
    # localtz = timezone('Europe/Lisbon')
    # dt_aware = localtz.localize(dt_unware)



def aware_time_to_utc(in_aware):

    import pytz

    utc_aware = in_aware.astimezone(pytz.timezone('UTC'))

    # print "utc_aware=", utc_aware
    return utc_aware





def utc_to_loc_time(in_tz_name, in_utc_time):

    import pytz

    local_timezone = pytz.timezone(in_tz_name)  # 'Europe/Kiev'
    loc_time = in_utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)

    # print "loc_time=", loc_time
    return loc_time



def loc_to_utc_time(in_tz_name, in_loc_time):

    import pytz

    loc_timezone = pytz.timezone(in_tz_name)
    loc_time = loc_timezone.localize(in_loc_time)
    utc_time = loc_time.astimezone(pytz.timezone('UTC'))

    # print "utc_time=", utc_time
    return utc_time






if __name__ == '__main__':


    place_name = 'Boston'
    coord = get_place_coord(place_name)
    print place_name, coord

    tz_name = get_tz_name(coord)
    print "tz_name=", tz_name


    format = "%Y-%m-%d %H:%M:%S %z"
    ###########################################################################
    utc_time = datetime.now()
    # utc_time = datetime.strptime("2011-06-21 02:37:21", "%Y-%m-%d %H:%M:%S")
    print "\nutc_time=", utc_time.strftime(format)

    loc_time = utc_to_loc_time(tz_name, utc_time)
    print "loc_time=", loc_time.strftime(format), "utcoffset=", loc_time.utcoffset()



    ###########################################################################
    loc_time = datetime.now()
    print "\nloc_time=", loc_time.strftime(format)

    utc_time = loc_to_utc_time(tz_name, loc_time)
    print "utc_time=", utc_time.strftime(format), "utcoffset=", utc_time.utcoffset()



    format = "%d %b %H:%M %z"
    format = "%Y-%m-%d %H:%M:%S %z"
    ###########################################################################
    loc_time = datetime.now()
    print "\nloc_time=", loc_time.strftime(format)

    aware_loc = set_tz_to_unaware_time(tz_name, loc_time)
    print "aware_loc=", aware_loc.strftime(format)
    print "aware_utc=", aware_time_to_utc(aware_loc).strftime(format)





    # from datetime import *
    # from dateutil import *
    # from dateutil.tz import *
    #
    # # METHOD 1: Hardcode zones:
    # utc_zone = dateutil.tz.gettz('UTC')
    # local_zone = tz.gettz('America/Chicago')
    # # METHOD 2: Auto-detect zones:
    # utc_zone = tz.tzutc()
    # local_zone = tz.tzlocal()
    #
    # # Convert time string to datetime
    # local_time = datetime.strptime("2008-09-17 14:02:00", '%Y-%m-%d %H:%M:%S')
    #
    # # Tell the datetime object that it's in local time zone since
    # # datetime objects are 'naive' by default
    # local_time = local_time.replace(tzinfo=local_zone)
    # # Convert time to UTC
    # utc_time = local_time.astimezone(utc_zone)
    # # Generate UTC time string
    # utc_string = utc_time.strftime('%Y-%m-%d %H:%M:%S')














