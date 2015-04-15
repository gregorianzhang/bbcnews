# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

urlli = []
urllib = []

keyword = sys.argv[1]
print keyword
def getnewurl(url):
    main = requests.get(url)
    soup = BeautifulSoup(main.text)
    main1 = soup.find_all('a', class_ = "global-navigation__action")
    for x in main1:
        urlli.append(x["href"])
#        print x["href"]
    getnewsurl(urlli)
#    print urlli

def getnewsurl(urllist):
#    print urllist
    for a in urllist:
        print a
        main = requests.get(a)
        soup = BeautifulSoup(main.text)
        main1 = soup.find_all('a', class_ ="u-faux-block-link__overlay")
        for x in main1:
            urllib.append(x["href"])

        getnews(urllib,keyword)

    

def getnews(urllist,keyword):
    for a in urllist:
        print a
        main = requests.get(a)
        soup = BeautifulSoup(main.text)
        title = soup.find("h1", class_ ="content__headline").text
        try:
            subheading = soup.find("div", class_ ="content__standfirst").p.text
        except AttributeError:
            subheading = ""
        try:
            maintext = soup.find("div", class_ ="content__article-body").text
        except AttributeError:
            maintext = ""


    if maintext.find(keyword) != -1:
        print  maintext
    else:
        pass

if __name__ == '__main__':
    url="http://www.theguardian.com/uk"
#    getnewurl(url)
    getnewurl(url)
