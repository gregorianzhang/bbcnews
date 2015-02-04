#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

#url = "http://www.bbc.com/news/health-31096218"
#url = "http://www.bbc.com/news/health-31069173"
#url = "http://www.bbc.com/news/business-31124076"

def getnews(url):
    content=""
    news = requests.get(url)
    if news.status_code == 200:
        # get url is OK
        #print "OK"
        soup = BeautifulSoup(news.text)
        #header = soup.h1.text
        header = soup.find("h1", class_="story-header").text
        try:
            bylinename = soup.find("span", class_="byline-name").text 
            bylinetitle = soup.find("span", class_="byline-title").text
            bylinephoto =  soup.find("span", class_="byline-photo").img["src"]
        except AttributeError:
            bylinename = ""
            bylinetitle = ""
            bylinephoto = ""

        main = soup.find("div", class_="story-body")
        for a in main.findAll('p'):
            if a.text != "Please turn on JavaScript. Media requires JavaScript to play.":
                content += a.text + "\n"
        image = [ x["src"] for x in main.findAll('img') ]

        return (header,bylinename,bylinetitle,bylinephoto,content,image)
        #return (header)

    else :
        # get url is error
        return "Error"

def getcategoryurl(url):
    #print url

    return url

def geturl(url):
    preurl="http://www.bbc.com"
    newurl = requests.get(url)
    if newurl.status_code == 200:
    #    print "OK"
        soup = BeautifulSoup(newurl.text)
        first = soup.find('div', id="top-story").a['href']
        second = soup.find('div', id="second-story").a['href']
        third = soup.find('div', id="third-story").a['href']
        return (preurl+first,preurl+second,preurl+third)
    else:
        return "Error"



if __name__ == '__main__':
#    print getnews(url)
#    aa=geturl('http://www.bbc.com/news/world/asia/china/')
#    for b in aa:
#        print getnews(b)
    print getcategoryurl('http://www.bbc.com/news')
#getnews(url)

