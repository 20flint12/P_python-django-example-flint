#!/usr/bin/env python

# https://dev.locu.com/console/
# 20flint12@gmail.com 87

# http://www.timeserver.ru/time.html

import requests
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#problems-after-installation
from bs4 import BeautifulSoup
import time



while 1:

    time.sleep(2)

    # r = requests.get("http://www.timeserver.ru/time.html")
    # # print r.content
    #
    # soup = BeautifulSoup(r.content)
    # # print soup.prettify()
    # # print soup.find_all("a")
    #
    # for link in soup.find_all("a"):
    #     # print link
    #     # print link.get('href')
    #     # print link.get("href")
    #
    #     # print link.text
    #     pass
    #     # print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
    #
    # g_data = soup.find_all("div", {"class": "time"})
    # # print g_data
    #
    # for item in g_data:
    #     # print item.text
    #     # print item
    #     print item.contents
    #     # print item.contents[1].text[2]


    # r = requests.get("http://www.moongiant.com/phase/today/")
    r = requests.get("http://www.calendar-365.com/moon/current-moon-phase.html")


    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()
    # print soup.find_all("a")

    # for link in soup.find_all("a"):
    #     # print link
    #     # print link.get('href')
    #     # print link.get("href")
    #
    #     # print link.text
    #     pass
    #     # print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

    # g_data = soup.find_all("div", id="moonDetails")

    # g_data = soup.find("div", {"id": "moonDetails"})
    # g_data = soup.find_all("div", {"id":"fullDateTitle"})
    g_data = soup.find_all("table", {"class":"table1"})
    # print g_data

    for table in g_data:
        trTags = table.find_all("tr")
        # print trTags

        for tag in trTags:
            print tag.text


    # for item in g_data:
    #     # print item.text
    #     # print item
    #     print item.contents
    #     # print item.contents[1].text[2]


