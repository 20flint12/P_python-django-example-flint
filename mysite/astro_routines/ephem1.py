# coding: utf8


import ephem
import datetime


def sun_rise():

    # pass
    now = datetime.datetime.now() #get current time

    Boston = ephem.Observer()
    Boston.pressure = 1010 # millibar
    Boston.temp = 25 # deg. Celcius
    Boston.horizon = 0
    Boston.lat = '42.3462'
    Boston.lon = '-71.0978'
    Boston.elevation = 3 # meters
    Boston.date = now

    sun = ephem.Sun()

    # print(Boston.next_rising(sun))
    # print(ephem.localtime(Boston.next_rising(sun)))

    str_out = ''
    str_out += "Next sunrise in Boston will be: " + \
               str(ephem.localtime(Boston.next_rising(sun))) + "\n"
    str_out += "Next sunset in Boston will be: " + \
               str(ephem.localtime(Boston.next_setting(sun)))

    # print(str_out)

    return str_out







# # '1978/10/3 11:32'
# d1 = ephem.next_full_moon('2015/3/14')
# print(d1)
# # 1984/1/18 14:05:10
# d2 = ephem.next_new_moon(d1)
# print"New moon:",d2




if __name__ == '__main__':

    sun_rise()