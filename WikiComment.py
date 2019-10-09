from bs4 import BeautifulSoup
import re
import urllib.request
import tweepy
import random

from PrivateKeys import *


OnlyAscii = lambda s: re.match('^[\x00-\x7F]+$', s) != None

#chooses random tweet from list of 50 containing requested string
def findTweet(search_results):
	pos = random.randint(0,49)
	#checks if valid (only contains ascii characters)
	if OnlyAscii(search_results[pos].text):
		return pos
	else:
		return findTweet(search_results)


url = 'https://en.wikipedia.org/wiki/special:random'
response = urllib.request.urlopen(url)

url = response.url
response = urllib.request.urlopen(url)

#"signing into account"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_results = api.search(q="what is", count=50)

twt2respond = search_results[findTweet(search_results)]
#print(twt2respond.text)

name = twt2respond.user.screen_name
reply = "@"+name+" "+url
twtid = twt2respond.id;
#print(reply)
#print(twtid)

api.update_status(reply, in_reply_to_status_id = twtid)