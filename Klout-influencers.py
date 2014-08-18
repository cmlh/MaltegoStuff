#!/usr/bin/python
#DESC: Transform Twitter entity into Twitter entities influencing the original
# Twitter ID to weighted influencers
# minor tweak
import sys, time, re
from MaltegoTransform import *
from pyklout import Klout

args = sys.argv[2].split("#")
names = args[2].split("=")
name = str(names[1])
name = re.sub(" ","",name)

# throttle to 8 calls/sec, should permit Maltego to chew through
# long lists of Twitter accounts w/o overrunning API limit
time.sleep(.125)

# https://klout.com/s/developers/home
# register an app, get an API key
# wil look something like this
api = Klout("xfv9wju86xn4wqsqzexample")

me = MaltegoTransform();

data = api.identity(name,'twitter')
user_id = data['id']

# fails hard if you feed it a name that doesn't have a Klout account
# really must find Python equivalent of Try::Tiny for this problem.
list = api.influences(user_id)

for inf in list['myInfluencers']:
    name = str(inf['entity']['payload']['nick']);
    score = str(int(inf['entity']['payload']['score']['score']));
    NewEnt = me.addEntity("AffiliationTwitter",name); 
    NewEnt.setWeight(score);
    NewEnt.addAdditionalFields("affiliation.uid","UID","",name);
    nurl = "http://twitter.com/" + name;
    NewEnt.addAdditionalFields("affiliation.profile-url","Profile URL","",nurl);
    NewEnt.addAdditionalFields("twitter.screen-name","Screen Name","",name);

me.returnOutput();
