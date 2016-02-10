#!/usr/bin/env python

import requests
import urllib
import threading
import time
from BeautifulSoup import BeautifulSoup

target = "http://ropas.snu.ac.kr/~kwang/4190.310/mooc/"
response = requests.get(target)
page = str(BeautifulSoup(response.content))

def getURL(page):
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def download(url, fileName):
    urllib.urlretrieve(url, fileName)
    print fileName + " download end"

while True:
    url, n = getURL(page)
    page = page[n:]

    if url:

        if url.endswith('.mp4'):

            while 10 < threading.activeCount():
                time.sleep(3)

            print url
            t = threading.Thread(target=download, args=(target+url, url))
            t.daemon = True
            t.start()

    else:
        while 0 < threading.activeCount():
            time.sleep(3)
        break
