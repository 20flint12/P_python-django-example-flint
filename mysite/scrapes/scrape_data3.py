# coding: utf8

import os
import urllib
import urllib2


import requests
from bs4 import BeautifulSoup
import time
import re


str_last_time = ""

def get_news():

    global str_last_time

    r = requests.get("http://korrespondent.net/")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()
    g_data = soup.find_all("div", {"class": "time-articles"})
    # print g_data

    str_news = ""
    for item in g_data:
        # print item
        # print item.text

        time_artTags = item.find("div", {"class": "article "})
        # print time_artTags.text

        str_news = time_artTags.text
        # print (str_news)


    # return unicode(str_news)

    if str_last_time == str_news:
        return None
    else:
        str_last_time = str_news
        return unicode(str_last_time)






if __name__ == '__main__':

    print (get_news())


