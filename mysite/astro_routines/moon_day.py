# coding: utf8
#!/usr/bin/python


import datetime
import ephem


def get_phase_on_day(date):
    """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""
    #Ephem stores its date numbers as floating points, which the following uses
    #to conveniently extract the percent time between one new moon and the next
    #This corresponds (somewhat roughly) to the phase of the moon.

    #Use Year, Month, Day as arguments
    # date=ephem.Date(datetime.date(year,month,day))

    pnm = ephem.previous_new_moon(date)
    nnm = ephem.next_new_moon(date)


    print "prev_new_moon:", pnm, "localtime:", str(ephem.localtime(pnm))[:19]
    print "next_new_moon:", nnm, "localtime:", str(ephem.localtime(nnm))[:19]

    lunation=(date-pnm)/(nnm-pnm)

    print "lunation:", lunation, "moon manth:",nnm-pnm

    #Note that there is a ephem.Moon().phase() command, but this returns the
    #percentage of the moon which is illuminated. This is not really what we want.

    return lunation


def get_moons_in_year(year):
    """Returns a list of the full and new moons in a year. The list contains tuples
    of either the form (DATE,'full') or the form (DATE,'new')"""
    moons=[]

    date=ephem.Date(datetime.date(year,01,01))
    while date.datetime().year==year:
        date=ephem.next_full_moon(date)
        moons.append( (date,'full moon') )

    date=ephem.Date(datetime.date(year,01,01))
    while date.datetime().year==year:
        date=ephem.next_new_moon(date)
        moons.append( (date,'new moon') )

    date=ephem.Date(datetime.date(year,01,01))
    while date.datetime().year==year:
        date=ephem.next_first_quarter_moon(date)
        moons.append( (date,'first_quarter') )

    date=ephem.Date(datetime.date(year,01,01))
    while date.datetime().year==year:
        date=ephem.next_last_quarter_moon(date)
        moons.append( (date,'last_quarter') )


    moons.sort(key=lambda x: x[0])

    return moons



date_now = ephem.now() # current UTC date and time
print get_phase_on_day(date_now)


# print get_moons_in_year(2013)
# for ev in get_moons_in_year(2015):
#     print ev