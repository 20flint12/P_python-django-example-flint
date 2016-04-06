# coding: utf8

import os
import urllib
import urllib2

import pprint

import requests
from bs4 import BeautifulSoup
import time
import re


str_last_time = u""

def get_solar_activity():

    global str_last_time

    r = requests.get("http://www.spaceweather.com/")
    # print r.content


    soup = BeautifulSoup(r.content)
    # print( soup.prettify() )

    # <table cellpadding="0" cellspacing="0"
    # bgcolor="#FFFFF0"
    # border="1" height="100" width="100%">
    g_data = soup.find_all("table", {"bgcolor": "#FFFFF0",
                                     "cellpadding": "0",
                                     "cellspacing": "0",
                                     "border":  "1",
                                     "height": "100"})
    # print "tables)", g_data
    total = []
    for item in g_data:
        # print item
        # print item.text

        slst = []
        trTags = item.find_all("tr")
        for tr in trTags:
            # print tr
            # print tr.text

            cnt = 0
            # sumt = "---"
            tlst = []
            tdTags = tr.find_all("td")
            for td in tdTags:
                txt = td.text
                txt = txt.replace("%","")
                txt = txt.rstrip("\n")
                # print "txt=", txt

                # sumt += " " + txt
                if txt in ["MINOR","ACTIVE","SEVERE"]:
                    cnt = 1
                    # print cnt, txt
                    tlst.append(txt)
                else:
                    if cnt > 0 and cnt < 3:
                        cnt += 1
                        # print cnt, pprint.pprint(txt)
                        # print cnt, txt
                        tlst.append(txt)
                    else:
                        break

            # print "sumt=", sumt
            if tlst:
                slst.append(tlst)

        # pprint.pprint(slst)
        total.append(slst)

    return total[0] # take first table





if __name__ == '__main__':

    print get_solar_activity()


