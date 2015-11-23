#!/usr/bin/env python
# -*- coding: utf-8 -*-


# http://stackoverflow.com/questions/16505501/get-timezone-from-city-in-python-django
# http://stackoverflow.com/questions/4563272/how-to-convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-stand


#
# from geopy import geocoders # pip install geopy
#
# from datetime import datetime
#
# import pytz
#
# from tzwhere import tzwhere
#
#
#
# g = geocoders.GoogleV3()
# place, (lat, lng) = g.geocode('Boston')     # Kremenchuk
# # -> (u'Singapore', (1.352083, 103.819836))
# print place, lat, lng
#
#
#
#
#
# w = tzwhere.tzwhere()
# # print w.tzNameAt(1.352083, 103.819836)
# # print w.tzNameAt(lat, lng)
# # -> Asia/Singapore
#
# tz_name = w.tzNameAt(lat, lng)
# print "tz_name=", tz_name
#
#
#
#
# # local_tz = pytz.timezone('Europe/Moscow') # use your local timezone name here
# # # NOTE: pytz.reference.LocalTimezone() would produce wrong result here
# # print "local_tz=", local_tz
#
#
#
# # local_timezone = pytz.timezone('Europe/Kiev')
# local_timezone = pytz.timezone(tz_name)
# utc_time = datetime.strptime("2011-06-21 02:37:21", "%Y-%m-%d %H:%M:%S")
# local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(local_timezone)
# print "local_time=", local_time
#
#
#
#
#
#
#
# # import datetime
# #
# # from django.utils import timezone
# # today = datetime.datetime.today()
# #
# # print "today=", today
# # # datetime.datetime(2014, 8, 1, 20, 15, 0, 513000, tzinfo=<UTC>)
# #
# # timezone.localtime(today)
# # print "timezone=", timezone
# # # datetime.datetime(2014, 8, 1, 16, 15, 0, 513000, tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>)
#



import ephem
# boston = ephem.city('Kharkiv')
# print('%s %s' % (boston.lat, boston.lon))
# 42:21:30.4 -71:03:35.2


# m = ephem.Moon()
# print(ephem.constellation(m))
# ('Aqr', 'Aquarius')



m = ephem.Moon('1980/6/1')
print(ephem.constellation(m))
# ('Sgr', 'Sagittarius')

print m.a_ra






