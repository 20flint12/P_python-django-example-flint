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
        print tr.text
        out_str += tr.text + "\n"


    # out_str = trTags[1].text

    # if str_last_time == out_str:
    #     return None
    # else:
    #     str_last_time = out_str
    #     return unicode(str_last_time)

    return unicode(out_str)





if __name__ == '__main__':

    print (get_temperature())