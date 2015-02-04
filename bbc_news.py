#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

#url = "http://www.bbc.com/news/health-31096218"
#url = "http://www.bbc.com/news/health-31069173"
#url = "http://www.bbc.com/news/business-31124076"

def getnews(url):
    print "--------------------------------------------------"
    print url
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
    allurl= []
    menu1 = []
    menu2 = []
    preurl = "http://www.bbc.com"
    urlall = requests.get(url)
    if urlall.status_code == 200:
        soup = BeautifulSoup(urlall.text)
        menu = soup.find_all('ul', class_="nav")
        for  x in menu[0].find_all('a'):
            if x["href"] == "/news/":
                pass
            else:
                if x["href"] == "/news/video_and_audio/":
                    pass
                else:
                    menu1.append(x["href"])
    else:
        return "Error"
    #print menu1

    for x in menu1:
        #print x
        url1 = requests.get(preurl + x)
        if url1.status_code == 200:
            #print url1.url
            soup = BeautifulSoup(url1.text)
            menu = soup.find_all('ul', class_="nav")
            if len(menu) >= 2:
                #print menu2
                #print "---------------------"
                for x in menu[1].find_all('a'):
                    if x["href"] == "/news/":
                        pass
                    else:
                        if x["href"] == "/news/business/market_data/":
                            pass
                            if x["href"] == "/news/business-11428889":
                                pass
                                if x["href"] == "/news/business-12686570":
                                    pass
                                else:
                                    menu2.append(x["href"])
        else:
            return "Error"
    
    #print "menu2 %s" % menu2   
    allurl = menu1 + menu2
    for x in allurl:
#        print x
        geturl(preurl + x)


def geturl(url):
    preurl="http://www.bbc.com"
    newurl = requests.get(url)
    #print "--------------------------------------"
    #print newurl.url
    if newurl.status_code == 200:
    #    print "OK"
        soup = BeautifulSoup(newurl.text)
        first = soup.find('div', id="top-story").a['href']
        second = soup.find('div', id="second-story").a['href']
        third = soup.find('div', id="third-story").a['href']
        #return (preurl+first,preurl+second,preurl+third)
        getnews(preurl+first)
        getnews(preurl+second)
        getnews(preurl+third)

    else:
        return "Error"



if __name__ == '__main__':
#    print getnews(url)
#    aa=geturl('http://www.bbc.com/news/world/asia/china/')
#    for b in aa:
#        print getnews(b)
    getcategoryurl('http://www.bbc.com/news')
#getnews(url)

