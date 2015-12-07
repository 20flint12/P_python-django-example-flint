# coding: utf8
#!/usr/bin/python


import datetime
import ephem
import pprint

import mysite.astro_routines.geo_place as geo
import mysite.astro_routines.geo_preload as geopr



def _set_Observer(coord):

    place = ephem.Observer() # Kharkov
    place.pressure = 1010 # millibar
    place.temp = 25 # deg. Celcius
    place.horizon = 0

    # place.lat = '50.0'
    # place.lon = '36.15'
    place.lat = str(coord[0])
    place.lon = str(coord[1])

    place.elevation = 3 # meters

    return place



def get_moonday(in_date_utc, coord):
    '''
    Input:
    Returns:
    '''
    
    place = _set_Observer(coord)
    moon = ephem.Moon()

    #####################################################################
    curr_date = ephem.Date(in_date_utc)
    prev_NM = ephem.previous_new_moon(in_date_utc)
    next_NM = ephem.next_new_moon(in_date_utc)

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

        str_out, md_dict = _form_str_moon_day(cur_mday,
                                             day_rise, day_sett, new_rise,
                                             str_mark)
        str_head += str_out + "\n"

    str_head += "<" * 80

    # print str_head, "\ncur_mday=", cur_mday

    return md_dict, str_head



def _form_str_moon_day(cur_day,
                      day_rise,day_sett,new_rise,
                      str_mark):
    str_out = ""
    str_out += "{:2d} =".format(cur_day)
    str_out += " rise:{0:<18}".format(str(day_rise))
    str_out += " set:{0:<18}".format(str(day_sett))
    str_out += " to:{0:<18}".format(str(new_rise))
    str_out += str_mark

    md_dict = {}
    md_dict["moon_day"] = cur_day
    md_dict["day_rise"] = day_rise
    md_dict["day_sett"] = day_sett
    md_dict["new_rise"] = new_rise

    return str_out, md_dict



def get_moonday_local12place(in_date_loc, place):
    """
    Input: local unaware time and place
    Returns tuple in utc for local time and place
    """

    tz_name, coord = geopr.set_tz(place)
    print "place=", place, coord, tz_name


    format = "%Y-%m-%d %H:%M:%S %z"
    ###########################################################################
    cur_date_loc = in_date_loc  # datetime.datetime.today()
    print "cur_date_loc=", cur_date_loc.strftime(format)

    # Calculate utc date on local noon for selected place #####################
    cur_noon_loc = datetime.datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
    print "cur_noon_loc=", cur_noon_loc
    # -------------------------------------------------------------------------

    aware_loc = geo.set_tz_to_unaware_time(tz_name, cur_noon_loc)
    print "aware_loc=", aware_loc.strftime(format)
    # -------------------------------------------------------------------------

    cur_date_utc = geo.aware_time_to_utc(aware_loc)
    # print "aware_utc=",    cur_date_utc.strftime(format)
    print "cur_date_utc=", cur_date_utc.strftime(format), "utcoffset=", cur_date_utc.utcoffset()
    # -------------------------------------------------------------------------

    tp_md, ctx2 = get_moonday(cur_date_utc, coord)
    # =========================================================================


    tp_md.update({"date_utc": cur_date_utc})
    tp_md.update({"aware_loc": aware_loc})

    day_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_md["day_rise"]).datetime())
    day_sett_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_md["day_sett"]).datetime())
    new_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_md["new_rise"]).datetime())
    tp_md.update({"day_rise_loc": day_rise_loc})
    tp_md.update({"day_sett_loc": day_sett_loc})
    tp_md.update({"new_rise_loc": new_rise_loc})

    # 'aware_loc': datetime.datetime(2015, 12, 4, 12, 0, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'day_rise': 42340.40295680378,
    # 'day_rise_loc': datetime.datetime(2015, 12, 3, 23, 40, 15, 467846, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'day_sett': 42340.93776006038,
    # 'day_sett_loc': datetime.datetime(2015, 12, 4, 12, 30, 22, 469216, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'moon_day': 23,
    # 'new_rise': 42341.44557255306,
    # 'new_rise_loc': datetime.datetime(2015, 12, 5, 0, 41, 37, 468584, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>)}

    return tp_md



def get_sun_on_month():

    # start_date_loc = ephem.Date('2015/4/27 12:00')
    # start_date_loc = datetime.datetime(2015,4,29,12)
    start_date_loc = datetime.date.today() #get current time

    # Correct to nearest Monday
    start_date_mon = _prev_weekday(start_date_loc,6)
    stop_date_loc  = start_date_mon + datetime.timedelta(days=35)

    start_date_eph = ephem.Date(start_date_mon)
    stop_date_eph  = ephem.Date(stop_date_loc)


    place_name = "Kharkiv"
    tz_name, coord = geopr.set_tz(place_name)
    print "place=", place_name, coord, tz_name

    place = _set_Observer(coord)
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
        # str_out2 += "rising Sun  :" + _print_UTC_time(day_rise)
        # str_out2 += "setting Sun :" + _print_UTC_time(day_sett)
        str_out2 += "\n"

        i += 1
        sun_dict = {}
        sun_dict["id"] = i
        sun_dict["day_rise"] = day_rise
        # sun_dict["str_day_rise"] = _print_UTC_time(day_rise)
        sun_dict["day_sett"] = day_sett
        # sun_dict["str_day_sett"] = _print_UTC_time(day_sett)

        total_list.append(sun_dict)

    # print str_out2
    return total_list



def _prev_weekday(adate, wd): # 6 - sunday
    # Find previous weekday
    while adate.weekday() != wd: # Mon-Fri are 0-4
        adate -= datetime.timedelta(days=1)
    return adate



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


    # cur_place = "Boston"
    cur_place = "Kharkiv"
    loc_date = datetime.datetime.today()

    tp_md_ext = get_moonday_local12place(loc_date, cur_place)
    print "tp_md_ext=\n", pprint.pprint(tp_md_ext)




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
