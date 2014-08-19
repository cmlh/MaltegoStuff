#!/usr/bin/python
#DESC: DTurl.py - Transform Domain entity to DomainTools URL
import sys
import urllib2
from MaltegoTransform import *

url = "https://whois.domaintools.com/" + sys.argv[1]
title = sys.argv[1]

me = MaltegoTransform();
NewEnt = me.addEntity("maltego.URL","DT:" + title); 
NewEnt.addAdditionalFields("url","URL","",url);
NewEnt.addAdditionalFields("title","Title","",title);
me.returnOutput();
