# coding: utf8
#!/usr/bin/python


import datetime
import ephem
import pprint

import mysite.config_ASR as conf



def set_Observer(in_day_utc, in_place):

    place = ephem.Observer() # Kharkov
    place.pressure = 1010 # millibar
    place.temp = 25 # deg. Celcius
    place.horizon = 0

    # place.lat = '50.0'
    # place.lon = '36.15'
    place.lat = str(conf.GEO_PLACE[in_place]["location"][0])
    place.lon = str(conf.GEO_PLACE[in_place]["location"][1])


    place.elevation = 3 # meters
    place.date = in_day_utc
    return place



def get_phase_on_current_day(in_date, in_place):
    """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""

    place = set_Observer(in_date, in_place)
    moon = ephem.Moon()

    #####################################################################
    curr_date = ephem.Date(in_date)
    prev_NM = ephem.previous_new_moon(in_date)
    next_NM = ephem.next_new_moon(in_date)

    str_head = ""
    str_head += "Calculate for UTC:{0:<18}\n".format(str(curr_date))
    str_head += "prev_NM : {:<18}\n".format(str(prev_NM))
    str_head += "next_NM : {:<18}\n".format(str(next_NM))
    str_head += ">" * 80 + "\n"

    cur_mday = 0
    place.date = prev_NM
    new_rise = place.next_rising(moon)

    md_dict = {}
    while curr_date > new_rise:
        str_mark = ""
        cur_mday += 1    # prepare for next moon day
        if cur_mday == 1:
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

        str_out, md_dict = form_str_moon_day(cur_mday,
                                             day_rise, day_sett, new_rise,
                                             str_mark)
        str_head += str_out + "\n"

    str_head += "<" * 80

    print str_head, "\ncur_mday=", cur_mday

    return md_dict, str_head, cur_mday



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
    md_dict["str_day_rise"] = _print_UTC_time(day_rise)
    md_dict["day_sett"] = day_sett
    md_dict["str_day_sett"] = _print_UTC_time(day_sett)
    md_dict["new_rise"] = new_rise
    md_dict["str_new_rise"] = _print_UTC_time(new_rise)

    return str_out, md_dict





def get_sun_on_month():

    # start_date = datetime.datetime.now() #get current time
    # start_date = ephem.Date(datetime.date(2015,4,1))
    # start_date = ephem.Date('2015/4/27 12:00')

    start_date_loc = datetime.datetime(2015,4,29,12)
    start_date_loc = datetime.date.today() #get current time

    # Correct to nearest Monday
    start_date_mon = _prev_weekday(start_date_loc,6)
    stop_date_loc  = start_date_mon + datetime.timedelta(days=35)

    start_date_eph = ephem.Date(start_date_mon)
    stop_date_eph  = ephem.Date(stop_date_loc)

    place = set_Observer(start_date_eph)
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
        str_out2 += "rising Sun  :" + _print_UTC_time(day_rise)
        str_out2 += "setting Sun :" + _print_UTC_time(day_sett)
        str_out2 += "\n"

        i += 1
        sun_dict = {}
        sun_dict["id"] = i
        sun_dict["day_rise"] = day_rise
        sun_dict["str_day_rise"] = _print_UTC_time(day_rise)
        sun_dict["day_sett"] = day_sett
        sun_dict["str_day_sett"] = _print_UTC_time(day_sett)

        total_list.append(sun_dict)

    # print str_out2
    return total_list



def _prev_weekday(adate,wd): # 6 - sunday
    # Find previous weekday
    while adate.weekday() != wd: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    return adate




def _print_UTC_time(time):

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
    # # # print get_phase_on_current_day2(date_now)


    # start_date = datetime.datetime.now()        # get current time
    # start_date -= datetime.timedelta(hours=3)   # always everything in UTC
    cur_date_utc = ephem.now()  # current UTC date and time
    pprint.pprint(get_phase_on_current_day(cur_date_utc))

    # dates = ('2015/5/18 3:00:00','2015/4/19 3:00:00','2015/5/19 4:00:00')
    # # print get_phase_on_current_day2(dates)
    # out_list = get_phase_on_current_day2(dates)
    # for key in out_list:
    #     print key,out_list[key]




    # out_list = get_sun_on_month()

    # for d in out_list:
    #     for k in sorted(d):
    #         print k, d[k]
    #     # print sorted(item),item

    # print get_moons_in_year(2013)
    # for ev in get_moons_in_year(2015):
    #     print ev
