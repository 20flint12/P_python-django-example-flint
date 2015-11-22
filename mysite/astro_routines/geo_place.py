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



def utc_to_local_time(in_tz_name, in_utc_time):

    import pytz

    local_timezone = pytz.timezone(in_tz_name)  # 'Europe/Kiev'
    local_time = in_utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)

    # print "local_time=", local_time
    return local_time





if __name__ == '__main__':


    utc_time = datetime.now()

    # utc_time = datetime.strptime("2011-06-21 02:37:21", "%Y-%m-%d %H:%M:%S")
    print "utc_time=", utc_time

    place_name = 'Boston'
    coord = get_place_coord(place_name)
    print place_name, coord

    tz_name = get_tz_name(coord)
    print "tz_name=", tz_name


    loc_time = utc_to_local_time(tz_name, utc_time)
    print "loc_time=", loc_time, loc_time.utcoffset()