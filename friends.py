#!/usr/bin/python
import twitter
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('twitter.cfg')
username = config.get('secrets','username')
password = config.get('secrets','password')
api = twitter.Api(username=username,password=password)
print "Friends:"
for u in api.GetFriends():
	print u.screen_name;

