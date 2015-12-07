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



def get_sun_rise_sett(in_date_utc, coord):
    '''
    Input:
    Returns:
    '''

    place = _set_Observer(coord)
    sun = ephem.Sun()

    #####################################################################
    place.date = in_date_utc

    day_rise = place.previous_rising(sun)
    day_sett = place.next_setting(sun)
    # ===============================================

    sun_dict = {}
    sun_dict["day_rise"] = day_rise
    sun_dict["day_sett"] = day_sett

    return sun_dict



def get_sun_rise_sett_local12place(in_date_loc, place):
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

    tp_srs = get_sun_rise_sett(cur_date_utc, coord)
    # =========================================================================


    tp_srs.update({"date_utc": cur_date_utc})
    tp_srs.update({"aware_loc": aware_loc})

    day_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_srs["day_rise"]).datetime())
    day_sett_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_srs["day_sett"]).datetime())
    tp_srs.update({"day_rise_loc": day_rise_loc})
    tp_srs.update({"day_sett_loc": day_sett_loc})

    # 'aware_loc': datetime.datetime(2015, 12, 7, 12, 0, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'date_utc': datetime.datetime(2015, 12, 7, 10, 0, tzinfo=<UTC>),
    # 'day_rise': 42343.72103858385,
    # 'day_rise_loc': datetime.datetime(2015, 12, 7, 7, 18, 17, 733644, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'day_sett': 42344.065384584246,
    # 'day_sett_loc': datetime.datetime(2015, 12, 7, 15, 34, 9, 228078, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>)}

    return tp_srs



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

    place = _set_Observer(start_date_eph)
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



def _print_UTC_time(time):

    out_str_time = ""
    out_str_time += "UTC:"
    out_str_time += str(time)
    out_str_time += " {" + str(ephem.localtime(time))[:19] + "}"

    return out_str_time






if __name__ == '__main__':


    # cur_place = "Boston"
    cur_place = "Kharkiv"
    loc_date = datetime.datetime.today()

    tp_md_ext = get_sun_rise_sett_local12place(loc_date, cur_place)
    print "tp_md_ext=\n", pprint.pprint(tp_md_ext)


    #
    # cur_place = "Boston"
    # # cur_place = "Kharkiv"
    #
    # tz_name, coord = geopr.set_tz(cur_place)
    # print "cur_place=", cur_place, coord, tz_name
    #
    #
    # format = "%Y-%m-%d %H:%M:%S %z"
    # ###########################################################################
    # cur_date_loc = datetime.datetime.today()
    # print "cur_date_loc=", cur_date_loc.strftime(format)
    #
    # # Calculate utc date on local noon for selected place #####################
    # cur_noon_loc = datetime.datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
    # print "cur_noon_loc=", cur_noon_loc
    #
    # aware_loc = geo.set_tz_to_unaware_time(tz_name, cur_noon_loc)
    # print "aware_loc=", aware_loc.strftime(format)
    # cur_date_utc = geo.aware_time_to_utc(aware_loc)
    # # print "aware_utc=",    cur_date_utc.strftime(format)
    # print "cur_date_utc=", cur_date_utc.strftime(format), "utcoffset=", cur_date_utc.utcoffset()
    #
    # sd = get_sun_rise_sett(cur_date_utc, coord)
    # print "sd=", pprint.pprint(sd)
    #
    #
    # str_msg = "sunrise - sunsett:\n"
    #
    # day_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(sd["day_rise"]).datetime())
    # day_sett_loc = geo.utc_to_loc_time(tz_name, ephem.Date(sd["day_sett"]).datetime())
    #
    # str_msg += "rise " + str(day_rise_loc.strftime(format)) + "\n"
    # str_msg += "sett " + str(day_sett_loc.strftime(format)) + "\n"
    #
    # print str_msg, " |||"*5, len(str_msg)
    #
