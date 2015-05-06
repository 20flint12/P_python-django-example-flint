# coding: utf8
#!/usr/bin/python


import datetime
import ephem

def get_interval_phase_on_day(start_day,end_day):
    pass


def get_phase_on_current_day(in_day):
    """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""

    #Use Year, Month, Day as arguments
    # date=ephem.Date(datetime.date(year,month,day))

    # pnm = ephem.previous_new_moon(in_day)
    # nnm = ephem.next_new_moon(in_day)

    # print "\nprev_new_moon:", pnm, "localtime:", str(ephem.localtime(pnm))[:19]
    # print "next_new_moon:", nnm, "localtime:", str(ephem.localtime(nnm))[:19]

    # lunation=(date-pnm)/(nnm-pnm)
    # print "lunation:", lunation, "moon month:",nnm-pnm
    # #Note that there is a ephem.Moon().phase() command, but this returns the
    # #percentage of the moon which is illuminated. This is not really what we want.


    place = ephem.Observer() # Kharkov
    place.pressure = 1010 # millibar
    place.temp = 25 # deg. Celcius
    place.horizon = 0
    place.lat = '50.0'
    place.lon = '36.15'
    place.elevation = 3 # meters
    # place.date = pnm

    sun = ephem.Sun()
    moon = ephem.Moon()

    #####################################################################

    # prev_NM = ephem.Date('2015/4/19 4:00:00')
    # next_NM = ephem.Date('2015/5/19 4:00:00')
    prev_NM = ephem.previous_new_moon(in_day)
    next_NM = ephem.next_new_moon(in_day)
    place.date = prev_NM

    str_head = ""
    str_head += "prev_NM : {:<18}\n".format(str(prev_NM))
    str_head += "next_NM : {:<18}\n".format(str(next_NM))

    prm = place.previous_rising(moon)
    psm = place.previous_setting(moon)
    nrm = place.next_rising(moon)
    nsm = place.next_setting(moon)

    md_vis = 0
    day_rise = 0
    day_sett = 0
    new_rise = 0
    cur_day = 0

    if prm > psm:
        md_vis = True
        day_rise = prm
        day_sett = nsm
        new_rise = nrm
        cur_day += 1
    else:
        md_vis = False
        day_rise = prm
        day_sett = psm
        new_rise = nrm

    str_head += "{:2d} =".format(cur_day)
    str_head += " rise:{0:<18}".format(str(day_rise))
    str_head += " set:{0:<18}".format(str(day_sett))
    str_head += " to:{0:<18}".format(str(new_rise))
    str_head += " v:" + str(md_vis)
    str_head += "\n" + "-" * 60 + "\n"

    current_date = ephem.Date('2015/4/29 5:00:00')
    str_head += "Calculate for date:{0:<18}\n".format(str(current_date))

    str_out = ""
    while place.date < next_NM:

        day_rise = place.next_rising(moon)
        place.date = day_rise
        day_sett = place.next_setting(moon)
        place.date = day_sett
        new_rise = place.next_rising(moon)

        if current_date < day_rise or current_date < day_sett:
            str_out += "*" * 60
            break
        else:
            cur_day += 1
            str_out += "{:2d} =".format(cur_day)
            str_out += " rise:{0:<18}".format(str(day_rise))
            str_out += " set:{0:<18}".format(str(day_sett))
            str_out += " to:{0:<18}".format(str(new_rise))
            str_out += "\n" # new line

    str_full = str_head + str_out
    print str_full
    # print "\n"

    # str_out2  = "Calculate on new moon:    " + str(place.date) + "\n"
    # # str_out2 += "previous_rising Sun  :" + show_time(place.previous_rising(sun))
    # # str_out2 += "next_setting Sun     :" + show_time(place.next_setting(sun))
    # str_out2 += "previous_rising Moon :" + show_time(place.previous_rising(moon))
    # str_out2 += "previous_settingMoon :" + show_time(place.previous_setting(moon))
    # str_out2 += "previous_transit Moon:" + show_time(place.previous_transit(moon))
    # str_out2 += "next_rising  Moon    :" + show_time(place.next_rising(moon))
    # str_out2 += "next_setting Moon    :" + show_time(place.next_setting(moon))
    # str_out2 += "next_transit Moon    :" + show_time(place.next_transit(moon))
    # str_out2 += "next_antitransit Moon:" + show_time(place.next_antitransit(moon))
    # # str_out2 += "pass                 :" + show_time(place.next_pass(moon))
    # print str_out2



def set_observer(in_day_utc):
    place = ephem.Observer() # Kharkov
    place.pressure = 1010 # millibar
    place.temp = 25 # deg. Celcius
    place.horizon = 0
    place.lat = '50.0'
    place.lon = '36.15'
    place.elevation = 3 # meters
    place.date = in_day_utc
    return place


def form_str_moon_day(cur_day,day_rise,day_sett,new_rise,str_mark):
    str_out = ""
    str_out += "{:2d} =".format(cur_day)
    str_out += " rise:{0:<18}".format(str(day_rise))
    str_out += " set:{0:<18}".format(str(day_sett))
    str_out += " to:{0:<18}".format(str(new_rise))
    str_out += str_mark

    md_dict = {}
    md_dict["moon_day"] = cur_day
    md_dict["day_rise"] = day_rise
    md_dict["str_day_rise"] = show_time(day_rise)
    md_dict["day_sett"] = day_sett
    md_dict["str_day_sett"] = show_time(day_sett)
    md_dict["new_rise"] = new_rise
    md_dict["str_new_rise"] = show_time(new_rise)

    return str_out,md_dict


def get_phase_on_current_day2(dates):
    """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""

    place = set_observer(dates[0])
    moon = ephem.Moon()

    #####################################################################
    curr_date = ephem.Date(dates[0])
    # prev_NM = ephem.Date(dates[1])
    # next_NM = ephem.Date(dates[2])
    prev_NM = ephem.previous_new_moon(dates[0])
    next_NM = ephem.next_new_moon(dates[0])
    str_head = ""
    str_head += "Calculate for UTC:{0:<18}\n".format(str(curr_date))
    str_head += "prev_NM : {:<18}\n".format(str(prev_NM))
    str_head += "next_NM : {:<18}\n".format(str(next_NM))
    str_head += ">" * 60 + "\n"

    cur_day = 1
    place.date = prev_NM
    new_rise = place.next_rising(moon)

    md_dict = {}
    while curr_date > new_rise:
        str_mark = ""
        if cur_day == 1:
            day_rise = place.previous_rising(moon)
            day_sett = place.previous_setting(moon)
            if day_rise > day_sett:
                day_sett = place.next_setting(moon)
            day_rise = place.previous_rising(moon)
            str_mark = " new moon >>>"
        else:
            day_rise = place.next_rising(moon)
            place.date = day_rise
            day_sett = place.next_setting(moon)
            place.date = day_sett
            new_rise = place.next_rising(moon)

            if next_NM < new_rise:
                str_mark = " >>> new moon"

        str_out, md_dict = form_str_moon_day(cur_day,day_rise,day_sett,new_rise,str_mark)
        str_head += str_out + "\n"
        cur_day += 1    # prepare for next moon day

    str_head += "<" * 60

    print str_head
    # print "\n"

    return md_dict,str_head





from datetime import timedelta

def prev_weekday(adate,wd): # 6 - sunday
    # Find previous weekday
    while adate.weekday() != wd: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate



def get_sun_on_month():

    # start_date = datetime.datetime.now() #get current time
    # start_date = ephem.Date(datetime.date(2015,4,1))
    # start_date = ephem.Date('2015/4/27 12:00')

    start_date_loc = datetime.datetime(2015,4,29,12)
    start_date_loc = datetime.date.today() #get current time

    # Correct to nearest Monday
    start_date_mon = prev_weekday(start_date_loc,6)
    stop_date_loc  = start_date_mon + timedelta(days=35)

    start_date_eph = ephem.Date(start_date_mon)
    stop_date_eph  = ephem.Date(stop_date_loc)

    place = set_observer(start_date_eph)
    sun = ephem.Sun()

    total_list = []
    str_out2 = ""

    new_rise = start_date_eph

    i = 0
    while stop_date_eph >= new_rise:

        day_rise = place.next_rising(sun)
        place.date = day_rise
        day_sett = place.next_setting(sun)
        place.date = day_sett
        new_rise = place.next_rising(sun)

        # ===============================================
        str_out2 += "rising Sun  :" + show_time(day_rise)
        str_out2 += "setting Sun :" + show_time(day_sett)
        str_out2 += "\n"

        i += 1
        sun_dict = {}
        sun_dict["id"] = i
        sun_dict["day_rise"] = day_rise
        sun_dict["str_day_rise"] = show_time(day_rise)
        sun_dict["day_sett"] = day_sett
        sun_dict["str_day_sett"] = show_time(day_sett)

        total_list.append(sun_dict)

    # print str_out2
    return total_list


# from datetime import date
# from math import radians as rad,degrees as deg
#
# import ephem
#
# g = ephem.Observer()
# g.name='Somewhere'
# g.lat=rad(52.0)  # lat/long in decimal degrees
# g.long=rad(5.2)
#
# m = ephem.Moon()
#
# g.date = date.today()# local time zone, I'm in UTC+1
# g.date -= ephem.hour # always everything in UTC
#
# for i in range(24*4): # compute position for every 15 minutes
#     m.compute(g)
#
#     nnm = ephem.next_new_moon(g.date)
#     pnm = ephem.previous_new_moon(g.date)
#     # for use w. moon_phases.ttf A -> just past  newmoon,
#     # Z just before newmoon
#     # '0' is full, '1' is new
#     # note that we cannot use m.phase as this is the percentage of the moon
#     # that is illuminated which is not the same as the phase!
#     lunation=(g.date-pnm)/(nnm-pnm)
#     symbol=lunation*26
#     if symbol < 0.2 or symbol > 25.8 :
#         symbol = '1'  # new moon
#     else:
#         symbol = chr(ord('A')+int(symbol+0.5)-1)
#
#     print(ephem.localtime(g.date).time(), deg(m.alt),deg(m.az),
#       ephem.localtime(g.date).time().strftime("%H%M"),
#       m.phase,symbol)
#     g.date += ephem.minute*15



def show_time(time):

    out_str_time = ""
    out_str_time += "UTC:"
    out_str_time += str(time)
    out_str_time += " {" + str(ephem.localtime(time))[:19] + "}"

    return out_str_time




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







if __name__ == '__main__':

    # date_now = ephem.now() # current UTC date and time
    # print get_phase_on_current_day(date_now)
    # print "$%#" * 20 + "\n"
    # # print get_phase_on_current_day2(date_now)


    start_date = datetime.datetime.now() #get current time
    start_date -= timedelta(hours=3) # always everything in UTC
    dates = (start_date,'2015/4/19 4:00:00','2015/5/19 4:00:00')
    print get_phase_on_current_day2(dates)

    # dates = ('2015/5/18 3:00:00','2015/4/19 3:00:00','2015/5/19 4:00:00')
    # # print get_phase_on_current_day2(dates)
    # out_list = get_phase_on_current_day2(dates)
    # for key in out_list:
    #     print key,out_list[key]




    out_list = get_sun_on_month()

    # for d in out_list:
    #     for k in sorted(d):
    #         print k, d[k]
    #     # print sorted(item),item

    # print get_moons_in_year(2013)
    # for ev in get_moons_in_year(2015):
    #     print ev
