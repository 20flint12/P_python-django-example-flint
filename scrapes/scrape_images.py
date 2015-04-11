#!/usr/bin/env python
# coding: utf8

import os
import urllib
# import urllib2


import requests
from bs4 import BeautifulSoup
import time
import re




def download_photo(img_url, filename):

    # if not os.path.exists(d):
    #     os.makedirs(d)

    # try:
    #     os.makedirs(d)
    # except OSError as exception:
    #     if exception.errno != errno.EEXIST:
    #         raise


    print ("********")
    print (os.getcwd())
    print ("========")


    try:
        image_on_web = urllib.urlopen(img_url)
        # print image_on_web
        if image_on_web.headers.maintype == 'image':
            # print "$$"
            buf = image_on_web.read()
            path = os.getcwd() + "storage/sdcard0"
            # path = os.getcwd() + "/scratched_images2"
            file_path = "%s/%s" % (path, filename)
            print ("file_path:", file_path)

            if not os.path.exists(path):
                os.makedirs(path)

            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            return False
    except:
        return False
    return True



last_image_url = ""
images_counter = 0

def get_images():

    global last_image_url, images_counter

    r = requests.get("http://korrespondent.net/")
    # print r.content

    soup = BeautifulSoup(r.content)
    # print soup.prettify()
    g_data = soup.find_all("img", {"class": "article__img"})

    # for item in g_data:
    #     img_url = item.get('src')
    #     print img_url

    # print g_data[0]

    img_url = g_data[0].get('src')
    # print "img_url:", img_url


    if last_image_url == img_url:

        return False

    else:
        last_image_url = img_url

        image_name = "image_file_{}.jpg".format(images_counter)
        download_photo(img_url, image_name)
        images_counter += 1

        return True




print (get_images())







# url = "http://icecat.biz/p/toshiba/pscbxe-01t00een/satellite-pro-notebooks-4051528049077-Satellite+Pro+C8501GR-17732197.html"
# html = urllib2.urlopen(url)
# soup = BeautifulSoup(html)
#
# imgs = soup.findAll("div", {"class":"thumb-pic"})
# print imgs
# for img in imgs:
#     imgUrl = img.a['href'].split("imgurl=")[0]
#     urllib.urlretrieve(imgUrl, os.path.basename(imgUrl))

