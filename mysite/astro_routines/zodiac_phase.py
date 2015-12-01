# coding: utf8
#!/usr/bin/python

import sys

import datetime
import ephem
import pprint

import mysite.config_ASR as conf
import mysite.astro_routines.geo_place as geo





# boston = ephem.city('Kharkiv')
# print('%s %s' % (boston.lat, boston.lon))
# 42:21:30.4 -71:03:35.2



# m = ephem.Moon('1980/6/1')
# print(ephem.constellation(m))
# # ('Sgr', 'Sagittarius')
#
# print m.a_ra




# deg = ephem.degrees
# >>> print deg(deg('270') + deg('180'))

from ephem import *
import datetime
import itertools
import math

# zodiac = 'AR TA GE CN LE VI LI SC SG CP AQ PI'.split()
zodiac = 'Овен Телец Близнецы Рак Лев Дева Весы Скорпион Стрелец Козерог Водолей Рыбы'.split()

def format_zodiacal_longitude(longitude):
    "Format longitude in zodiacal form (like '00AR00') and return as a string."
    l = math.degrees(longitude.norm)
    degrees = int(l % 30)
    sign = zodiac[int(l / 30)]
    minutes = int(round((l % 1) * 60))
    return '{0:02}{1}{2:02}'.format(degrees, sign, minutes)

def format_angle_as_time(a):
    """Format angle as hours:minutes:seconds and return it as a string."""
    a = math.degrees(a) / 15.0
    hours = int(a)
    minutes = int((a % 1) * 60)
    seconds = int(((a * 60) % 1) * 60)
    return '{0:02}:{1:02}:{2:02}'.format(hours, minutes, seconds)

def print_ephemeris_for_date(date, bodies):
    date = Date(date)
    print datetime.datetime(*date.tuple()[:3]).strftime('%A')[:2],
    print '{0:02}'.format(date.tuple()[2]),
    greenwich = Observer()
    greenwich.date = date
    print format_angle_as_time(greenwich.sidereal_time()),
    for b in bodies:
        b.compute(date, date)
        print format_zodiacal_longitude(Ecliptic(b).long),
    print

def print_ephemeris_for_month(year, month, bodies):
    print
    print (datetime.date(year, month, 1).strftime('%B %Y').upper()
           .center(14 + len(bodies) * 7))
    print
    print 'DATE  SID.TIME',
    for b in bodies:
        print '{0: <6}'.format(b.name[:6].upper()),
    print
    for day in itertools.count(1):
        try:
            datetuple = (year, month, day)
            datetime.date(*datetuple)
            print_ephemeris_for_date(datetuple, bodies)
        except ValueError:
            break

def print_ephemeris_for_year(year):
    bodies = [Sun(), Moon(), Mercury(), Venus(), Mars(), Jupiter(),
              Saturn(), Uranus(), Neptune(), Pluto()]
    for month in xrange(1, 13):
        print_ephemeris_for_month(year, month, bodies)
        print



start_date = ephem.Date('2015/10/21 15:00')
stop_date  = ephem.Date('2016/02/21 15:00')

deg = ephem.degrees
cur_date = start_date

while stop_date >= cur_date:

    # print cur_date
    m = ephem.Moon(cur_date)
    print cur_date, m.ra, "deg=", deg(deg(m.ra)), \
        m.dec, deg(deg(m.dec)), \
        ephem.constellation(m), "|||", Ecliptic(m).long, Ecliptic(m).lat

    m.compute(cur_date, cur_date)
    print format_zodiacal_longitude(Ecliptic(m).long)

    cur_date = ephem.Date(cur_date + 0.1)
    # ===============================================


























