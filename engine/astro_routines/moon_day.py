
# coding: utf8
#!/usr/bin/python


import datetime
import ephem
import pprint
import re

import engine.astro_routines.geo_place as geo
import engine.astro_routines.geo_preload as geopr


def _set_Observer(coord):

    place = ephem.Observer()    # Kharkov
    place.pressure = 1010       # millibar
    place.temp = 25             # deg. Celcius
    place.horizon = 0

    # place.lat = '50.0'
    # place.lon = '36.15'
    place.lat = str(coord[0])
    place.lon = str(coord[1])

    place.elevation = 3     # meters

    return place


def get_moon_day(in_date_utc, coord):
    '''
    Input:
    Returns:
    '''
    
    place = _set_Observer(coord)
    moon = ephem.Moon()

    # print "in_date_utc=", in_date_utc

    #####################################################################
    curr_date = ephem.Date(in_date_utc)
    prev_NM = ephem.previous_new_moon(in_date_utc)
    next_NM = ephem.next_new_moon(in_date_utc)

    str_head = ""
    str_head += "Calculate for UTC:{0:<18}\n".format(str(curr_date))
    str_head += "prev_NM : {:<18}\n".format(str(prev_NM))
    str_head += "next_NM : {:<18}\n".format(str(next_NM))
    str_head += ">" * 80 + "\n"

    cur_mday = 1
    place.date = prev_NM
    day_rise = place.previous_rising(moon)
    day_sett = place.previous_setting(moon)
    new_rise = place.next_rising(moon)

    # print "curr_date > new_rise", curr_date, new_rise

    md_dict = {}
    md_dict["moon_day"] = cur_mday
    md_dict["day_rise"] = day_rise
    md_dict["day_sett"] = day_sett
    md_dict["new_rise"] = new_rise

    while curr_date > new_rise:
        str_mark = ""

        if cur_mday == 1:
            day_rise = place.previous_rising(moon)
            day_sett = place.previous_setting(moon)
            if day_rise > day_sett:
                day_sett = place.next_setting(moon)
            str_mark = " new moon >>>"
        else:
            day_rise = place.next_rising(moon)
            place.date = day_rise
            day_sett = place.next_setting(moon)
            place.date = day_sett
            new_rise = place.next_rising(moon)

            if next_NM < new_rise:
                str_mark = " >>> new moon"

        # print "day_rise=", day_rise

        str_out, md_dict = _form_str_moon_day(cur_mday,
                                              day_rise, day_sett, new_rise,
                                              str_mark)
        cur_mday += 1  # prepare for next moon day

        str_head += str_out + "\n"
        # print str_head

    str_head += "<" * 80

    # print str_head, "\ncur_mday=", cur_mday

    return md_dict, str_head


def _form_str_moon_day(cur_day,
                       day_rise, day_sett, new_rise,
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


# def get_moon_day_local12place(in_date_loc, place):
def get_moon_day_ext(in_aware_loc, in_unaware_utc, place):

    """
    Input: local unaware time and place
    Returns tuple in utc for local time and place
    """

    tz_name, coord = geopr.set_tz(place)
    # print "place=", place, coord, tz_name

    # print "in_aware_loc=", in_aware_loc.strftime(format), "utcoffset=", in_aware_loc.utcoffset()
    # print "in_unaware_utc=", in_unaware_utc
    # -------------------------------------------------------------------------

    tp_md_ext, ctx2 = get_moon_day(in_unaware_utc, coord)
    # =========================================================================
    # print "&^%$"*20, "\ntp_md_ext", tp_md_ext, ctx2

    tp_md_ext.update({"date_utc": in_unaware_utc})
    tp_md_ext.update({"aware_loc": in_aware_loc})

    day_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_md_ext["day_rise"]).datetime())
    day_sett_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_md_ext["day_sett"]).datetime())
    new_rise_loc = geo.utc_to_loc_time(tz_name, ephem.Date(tp_md_ext["new_rise"]).datetime())
    tp_md_ext.update({"day_rise_loc": day_rise_loc})
    tp_md_ext.update({"day_sett_loc": day_sett_loc})
    tp_md_ext.update({"new_rise_loc": new_rise_loc})

    # 'aware_loc': datetime.datetime(2015, 12, 4, 12, 0, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'day_rise': 42340.40295680378,
    # 'day_rise_loc': datetime.datetime(2015, 12, 3, 23, 40, 15, 467846, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'day_sett': 42340.93776006038,
    # 'day_sett_loc': datetime.datetime(2015, 12, 4, 12, 30, 22, 469216, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>),
    # 'moon_day': 23,
    # 'new_rise': 42341.44557255306,
    # 'new_rise_loc': datetime.datetime(2015, 12, 5, 0, 41, 37, 468584, tzinfo=<DstTzInfo 'Europe/Kiev' EET+2:00:00 STD>)}

    return tp_md_ext


def get_moons_in_year(year):
    """Returns a list of the full and new moons in a year. The list contains tuples
    of either the form (DATE,'full') or the form (DATE,'new')"""
    moons=[]

    date=ephem.Date(datetime.date(year, 1, 1))
    while date.datetime().year==year:
        date=ephem.next_full_moon(date)
        moons.append( (date,'full moon') )

    date=ephem.Date(datetime.date(year, 1, 1))
    while date.datetime().year==year:
        date=ephem.next_new_moon(date)
        moons.append( (date,'new moon') )

    date=ephem.Date(datetime.date(year, 1, 1))
    while date.datetime().year==year:
        date=ephem.next_first_quarter_moon(date)
        moons.append( (date,'first_quarter') )

    date=ephem.Date(datetime.date(year, 1, 1))
    while date.datetime().year==year:
        date=ephem.next_last_quarter_moon(date)
        moons.append( (date,'last_quarter') )

    moons.sort(key=lambda x: x[0])

    return moons


def get_moon_phase(in_date_utc):
    """
    :param in_date_utc:
    :return:
    """
    moon = ephem.Moon()

    #####################################################################
    curr_date = ephem.Date(in_date_utc)

    prev_NM = ephem.previous_new_moon(curr_date)
    prev_FQ = ephem.previous_first_quarter_moon(curr_date)
    prev_FM = ephem.previous_full_moon(curr_date)
    prev_LQ = ephem.previous_last_quarter_moon(curr_date)
    delta_prev_NM = curr_date - prev_NM
    delta_prev_FQ = curr_date - prev_FQ
    delta_prev_FM = curr_date - prev_FM
    delta_prev_LQ = curr_date - prev_LQ

    next_NM = ephem.next_new_moon(curr_date)
    next_FQ = ephem.next_first_quarter_moon(curr_date)
    next_FM = ephem.next_full_moon(curr_date)
    next_LQ = ephem.next_last_quarter_moon(curr_date)
    delta_next_NM = next_NM - curr_date
    delta_next_FQ = next_FQ - curr_date
    delta_next_FM = next_FM - curr_date
    delta_next_LQ = next_LQ - curr_date

    mph_dict = {}
    mph_dict["date_utc"] = curr_date
    #==========================================================================

    delta_prev = delta_prev_NM
    mph_dict["prev"] = "prev_NM"
    mph_dict["prev_NM_utc"] = prev_NM

    if delta_prev > delta_prev_FQ:
        delta_prev = delta_prev_FQ
        mph_dict["prev"] = "prev_FQ"
        mph_dict["prev_FQ_utc"] = prev_FQ

    if delta_prev > delta_prev_FM:
        delta_prev = delta_prev_FM
        mph_dict["prev"] = "prev_FM"
        mph_dict["prev_FM_utc"] = prev_FM

    if delta_prev > delta_prev_LQ:
        # delta_prev = delta_prev_LQ
        mph_dict["prev"] = "prev_LQ"
        mph_dict["prev_LQ_utc"] = prev_LQ
    #==========================================================================

    delta_next = delta_next_NM
    mph_dict["next"] = "next_NM"
    mph_dict["next_NM_utc"] = next_NM

    if delta_next > delta_next_FQ:
        delta_next = delta_next_FQ
        mph_dict["next"] = "next_FQ"
        mph_dict["next_FQ_utc"] = next_FQ

    if delta_next > delta_next_FM:
        delta_next = delta_next_FM
        mph_dict["next"] = "next_FM"
        mph_dict["next_FM_utc"] = next_FM

    if delta_next > delta_next_LQ:
        # delta_next = delta_next_LQ
        mph_dict["next"] = "next_LQ"
        mph_dict["next_LQ_utc"] = next_LQ
    # =========================================================================

    return mph_dict


def get_moon_phase_local12place(in_date_loc, place):
    """
    Input: local unaware time and place
    Returns tuple in utc for local time and place
    """

    tz_name, coord = geopr.set_tz(place)
    # print "place=", place, coord, tz_name


    format = "%Y-%m-%d %H:%M:%S %z"
    ###########################################################################
    cur_date_loc = in_date_loc  # datetime.datetime.today()
    # print "cur_date_loc=", cur_date_loc.strftime(format)

    # Calculate utc date on local noon for selected place #####################
    cur_noon_loc = datetime.datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
    # print "cur_noon_loc=", cur_noon_loc
    # -------------------------------------------------------------------------

    aware_loc = geo.set_tz_to_unaware_time(tz_name, cur_noon_loc)
    # print "aware_loc=", aware_loc.strftime(format)
    # -------------------------------------------------------------------------

    cur_date_utc = geo.aware_time_to_utc(aware_loc)
    # print "aware_utc=",    cur_date_utc.strftime(format)
    # print "cur_date_utc=", cur_date_utc.strftime(format), "utcoffset=", cur_date_utc.utcoffset()
    # -------------------------------------------------------------------------

    tp_mph = get_moon_phase(cur_date_utc)
    # =========================================================================
    # print "tp_mph=", pprint.pprint(tp_mph)

    for k in tp_mph.keys():
        # print k, "5%%%%%%%%%%%%%%%%%"

        str_re = "(.*)_utc"
        res = re.search(str_re, k)
        if res:
            time_item = res.group(1)
            time_item_loc = time_item + "_loc"

            time_utc = tp_mph[k]
            time_loc = geo.utc_to_loc_time(tz_name, ephem.Date(time_utc).datetime())

            tp_mph[time_item_loc] = time_loc


    # tp_mph.update({"date_utc": cur_date_utc})
    tp_mph.update({"aware_loc": aware_loc})

    # 'aware_loc': datetime.datetime(2015, 12, 11, 12, 0, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>),
    # 'date_loc': datetime.datetime(2015, 12, 11, 12, 0, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>),
    # 'date_utc': 42348.208333333336,
    # 'next': 'next_FQ',
    # 'next_FQ_loc': datetime.datetime(2015, 12, 18, 10, 14, 19, 81533, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>),
    # 'next_FQ_utc': 42355.1349430733,
    # 'prev': 'prev_NM',
    # 'prev_NM_loc': datetime.datetime(2015, 12, 11, 5, 29, 25, 28389, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 STD>),
    # 'prev_NM_utc': 42347.93709523599

    return tp_mph




if __name__ == '__main__':

    cur_place = "Boston"
    # cur_place = "Kharkiv"
    loc_date = datetime.datetime.today()

    # tp_md_ext = get_moon_day_local12place(loc_date, cur_place)
    # print "tp_md_ext=\n", pprint.pprint(tp_md_ext)

    print(get_moon_phase(loc_date))

    # for ev in get_moons_in_year(2015):
    #     print ev

    res_dict = get_moon_phase_local12place(loc_date, cur_place)
    pprint.pprint(res_dict)




