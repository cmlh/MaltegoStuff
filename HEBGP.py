#!/usr/bin/python
#DESC: HEBGP.py - Transform AS entity to Hurricane Electric AS url
import sys
import urllib2
from MaltegoTransform import *

title = str(sys.argv[1])

url = "http://bgp.he.net/AS" + title
me = MaltegoTransform();
NewEnt = me.addEntity("maltego.URL","AS" + title); 
NewEnt.addAdditionalFields("url","URL","",url);
NewEnt.addAdditionalFields("title","Title","","AS"+title);
me.returnOutput();
