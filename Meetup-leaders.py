#!/usr/bin/python
#DESC: Transform Meetup group URL into Meetup leader profile URLs
import httplib2, urllib2, lxml, sys, re
from bs4 import BeautifulSoup
from MaltegoTransform import *

baseurl = sys.argv[1]
url = sys.argv[1] + "members/?op=leaders"

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
soup = BeautifulSoup(opener.open(url),"lxml")

me = MaltegoTransform();

for thing in soup.find_all("a","memName"):
    NewEnt = me.addEntity("maltego.URL",thing.text + " Meetup"); 
    NewEnt.addAdditionalFields("url","URL","",thing['href']);
    

me.returnOutput();

