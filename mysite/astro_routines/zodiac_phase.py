# coding: utf8
#!/usr/bin/python


import sys

import datetime
import ephem
import pprint

import time

# import mysite.config_ASR as conf
# import mysite.astro_routines.geo_place as geo


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

# cur_date = start_date
# while stop_date >= cur_date:
#
#     # print cur_date
#     body = ephem.Moon(cur_date)
#     body.compute(cur_date, cur_date)
#
#     str_pr = str(body) + " "
#     str_pr += "deg={:>15}".format(deg(body.ra)) + " - "
#     str_pr += "deg={:>15}".format(deg(body.a_ra)) + " - "
#     str_pr += "deg={:>15}".format(deg(body.g_ra)) + " "
#     # str_pr += "deg={:7.2f}".format(deg(deg(body.ra)))+ ""
#
#     str_pr += "deg={:>15}".format(deg(body.dec)) + " + "
#     str_pr += "deg={:>15}".format(deg(body.a_dec)) + " + "
#     str_pr += "deg={:>15}".format(deg(body.g_dec)) + " "
#
#     str_pr += ephem.constellation(body)[0]
#     str_pr += " ||| "
#     str_pr += str(Ecliptic(body, epoch='2015').long)
#     str_pr += " ??? "
#     str_pr += str(Ecliptic(body, epoch='1950').long)
#     print str_pr
#
#     # print format_zodiacal_longitude(Ecliptic(body, epoch='2000').long)
#
#     cur_date = ephem.Date(cur_date + 1.5)
#     # ===============================================









#     >>> import ephem
#     >>> m = ephem.Mars('1990/12/13')
#     >>> print('%s %s' % (m.a_ra, m.a_dec))
#     3:51:20.54 22:12:49.4
#
#     >>> ecl = ephem.Ecliptic(m)
#     >>> print('%s %s' % (ecl.lon, ecl.lat))
#     60:27:09.2 2:00:47.5
#
#     >>> gal = ephem.Galactic(m)
#     >>> print('%s %s' % (gal.lon, gal.lat))
#     168:47:15.2 -24:14:01.8
#
#     The epoch of the resulting coordinates is the same as that used by the body for its astrometric coordinates:
#
#     >>> print(ecl.epoch)
#     2000/1/1 12:00:00
#
# Using Another Right Ascension and Declination
#
#     In the first above example, when we passed a body directly to Ecliptic() and Galactic(), they automatically used the body’s astrometric right ascension and declination. If for some particular application you want to use the apparent version of the coordinates instead, then use the alternative right ascension and declination to build your own Equatorial object:
#
#     >>> import ephem
#     >>> m = ephem.Mars('1980/2/25')
#     >>> ma = ephem.Equatorial(m.ra, m.dec, epoch='1980/2/25')
#     >>> me = ephem.Ecliptic(ma)
#     >>> print('%s %s' % (me.lon, me.lat))
#     155:52:22.4 4:22:08.7




def getInfo(body):

    str_out = "\n"
    str_out += str(body)
    str_out += " " + ephem.constellation(body)[0]
    # -----------------------------------------------------


    ma = ephem.Equatorial(body.ra, body.dec)
    me = ephem.Ecliptic(ma)

    ecl = ephem.Ecliptic(body, epoch=cur_date)


    str_out += "\n" + str(ma.epoch)

    str_out += " body.ra =" + str(deg(body.ra)) + " / " + str(deg(body.dec))
    str_out += " & deg={:7.3f}".format(body.ra * 180 / 3.14) + " - "
    # str_out += " ||| " + str(Ecliptic(body).long)


    str_out += " Equatorial ma.ra=" + str(ma.ra) + "=" + str(ma.dec)



    str_out += " me.lon =" + str(deg(me.lon))
    str_out += " & deg={:7.3f}".format(me.lon * 180 / 3.14) + " - "



    str_out += "\n" + str(ecl.epoch)
    str_out += " ecl.lon =" + str(ecl.lon) + " / " + str(ecl.lat)
    str_out += " & deg={:7.3f}".format(ecl.lon * 180 / 3.14) + " - "
    # ---------------------------------------------------------------------

    # body.compute(cur_date, cur_date)
    # print format_zodiacal_longitude(Ecliptic(body, epoch='2000').long)

    return str_out





if __name__ == "__main__":


    deg = ephem.degrees

    cur_date = start_date
    cur_date = ephem.Date(datetime.datetime.now())
    # while stop_date >= cur_date:
    while True:

        cur_date = ephem.Date(datetime.datetime.now())
        # print cur_date

        body = ephem.Moon(cur_date)
        # ---------------------------------------------------------------------

        str_out = ""
        str_out += getInfo(body)


        body = ephem.Sun(cur_date)
        # body.compute(cur_date, cur_date)

        str_out += getInfo(body)

        print str_out

        time.sleep(1)


        # cur_date = ephem.Date(cur_date + 0.5)
        # ===============================================







print("=============== END ====================")


# http://lyna.info/


# http://time.unitarium.com/moon/where.html
# http://www.satellite-calculations.com/Satellite/suncalc.htm
# http://www.moonsystem.to/justnowe.htm

# https://www.calsky.com/cs.cgi



