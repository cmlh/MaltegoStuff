#!/usr/bin/python
#DESC: Transform Twitter entity into Klout topic URLs
import sys
import time
from MaltegoTransform import *
from pyklout import Klout

# throttle to 8 calls/sec, should permit Maltego to chew through
# long lists of Twitter accounts w/o overrunning API limit
time.sleep(.125)

# https://klout.com/s/developers/home
# register an app, get an API key
# wil look something like this
api = Klout("xfv9wju86xn4wqsqzexample")

name = str(sys.argv[1])

me = MaltegoTransform();

data = api.identity(name,'twitter')
list = api.topics(data['id'])

for topic in list:
    name =topic['displayName']
    slug =topic['slug']
    NewEnt = me.addEntity("maltego.URL",name); 
    NewEnt.addAdditionalFields("url","URL","","http://klout.com/topic/" + slug);

me.returnOutput();
