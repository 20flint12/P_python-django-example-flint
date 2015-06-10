# coding: utf8


import requests
from bs4 import BeautifulSoup
import time
import re


# while True:
#
#
#
#     # r = requests.get("http://www.timeanddate.com/moon/usa/atlanta")
#     # # print r.content
#     #
#     # soup = BeautifulSoup(r.content)
#     # # print soup.prettify()
#     #
#     # g_data = soup.find_all("div", {"id": "qfacts"})
#     #
#     # for pTags in g_data:
#     #     ptags = pTags.find_all("p")
#     #     # print ptags
#     #
#     # #     for tag in ptags:
#     # #         print (tag.text)
#     # #
#     # # print ("-"*40)
#     #
#     #
#     #
#     #
#     #
#     # r = requests.get("https://www.heavens-above.com/moon.aspx?lat=0&lng=0&loc=Unspecified&alt=0&tz=CET")
#     # # print r.content
#     #
#     # soup = BeautifulSoup(r.content)
#     # # print soup.prettify()
#     #
#     # g_data = soup.find_all("td", {"valign": "top"})
#     # # # print g_data[0]
#     # # # print "\n"*10
#     # # print g_data[1]
#     # # print "\n"*10
#     # # print g_data[2]
#     # # print "\n"*10
#     #
#     #
#     # tableTags = g_data[1].find_all("table")
#     #
#     # for table in tableTags:
#     #
#     #     trTags = table.find_all("tr")
#     #     # print trTags
#     # #
#     # #     for tag in trTags:
#     # #         print (tag.text)
#     # #
#     # #
#     # # print ("="*40)
#     #
#     #
#     #
#
#
#
#     r = requests.get("http://meteopost.com/weather/kharkov/")
#     # print r.content
#
#     soup = BeautifulSoup(r.content)
#     # print soup.prettify()
#     #
#     #
#     # g_data = soup.find_all("table", {"id": "maint"})
#     g_data = soup.find_all("table")
#
#     # print g_data
#
#     # print g_data[0]
#     # print "\n"
#     # print "1#"*40
#     # print g_data[1]
#     # print "\n"
#     # print "2#"*40
#     # print g_data[2]
#     # print "\n"
#     # print "3#"*40
#
#     tabTags = g_data[2].find_all("table")
#
#     trTags = tabTags[1].find_all("tr")
#     for tr in trTags:
#         print tr.text
#
#         # line = u(tr.text)
#         str_re = u"Давление (на станции) (.*) мм.рт.ст."
#         # res = re.search(str_re, str)
#         # if res:
#         #     print res.group(1)  # pressure
#
#
#     # print "4#"*40
#     #
#     # trTags = tabTags[2].find_all("tr")
#     # for tr in trTags:
#     #     print tr.text
#     # print "5#"*40
#
#
#     time.sleep(5)
#


str_last_time = ""

def get_temperature():

    global str_last_time
    r = requests.get("http://meteopost.com/weather/kharkov/")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()
    g_data = soup.find_all("table")
    # print g_data

    tabTags = g_data[2].find_all("table")

    trTags = tabTags[1].find_all("tr")

    out_str = ""
    for tr in trTags:
        # print tr.text
        out_str += tr.text + "\n"


    # out_str = trTags[1].text

    # if str_last_time == out_str:
    #     return None
    # else:
    #     str_last_time = out_str
    #     return unicode(str_last_time)

    return unicode(out_str)




def parse_temperature(str_in):

    str_in = str_in.replace("\n", " ")
    print str_in

    # Погода в Харькове на14:30 Kyiv
    # Температура воздуха +29°
    # Температура комфорта +28°
    # Точка росы +8°
    # Влажность 27%
    # Давление (на уровне моря) 765 мм.рт.ст.
    # Давление (на станции) 752 мм.рт.ст.
    # Ветер западный
    # Скорость ветра 3 м/с
    # Пог. явления нет
    # Облачность кучево-дождевых облаков нет
    # Видимость >10 км
    # Изменения погоды (на 30 мин) не ожидаются
    # Характер погоды

    str_re = u"Погода в Харькове на(.*) Kyiv " \
             u"Температура воздуха (.*)° " \
             u"Температура комфорта (.*)° " \
             u"Точка росы (.*)° " \
             u"Влажность (.*)% " \
             u"Давление \(на уровне моря\) (.*) мм.рт.ст. " \
             u"Давление \(на станции\) (.*) мм.рт.ст. " \
             u"Ветер (.*)"


    res = re.search(str_re, str_in, flags=re.UNICODE)
    # print "=" * 50, "\n", res

    if res:
        # print "1)", res.group(1)  # time
        # print "2)", res.group(2)  # t_air
        # print "3)", res.group(3)  # t_com
        # print res.group(4)  #   t_dew
        # print res.group(5)  #   t_hum
        # print res.group(6)  #   p_sea
        # print res.group(7)  #   p_stn

        time = res.group(1)
        t_air = int(res.group(2))
        t_com = int(res.group(3))
        t_dew = int(res.group(4))
        t_hum = int(res.group(5))
        p_sea = int(res.group(6))
        p_stn = int(res.group(7))

        tmp_lst = []
        tmp_lst.append(time)
        tmp_lst.append(t_air)
        tmp_lst.append(t_com)
        tmp_lst.append(t_dew)
        tmp_lst.append(t_hum)
        tmp_lst.append(p_sea)
        tmp_lst.append(p_stn)

        return tmp_lst








if __name__ == '__main__':

    get_str = get_temperature()
    print get_str

    print parse_temperature(get_str)




















