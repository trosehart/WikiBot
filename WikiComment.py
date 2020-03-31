from bs4 import BeautifulSoup
import re
import urllib.request
import tweepy
import random

from PrivateKeys import *


OnlyAscii = lambda s: re.match('^[\x00-\x7F]+$', s) != None

#chooses random tweet from list of 50 containing requested string
def findTweet(search_results,num_results):

    if num_results == 0:
        return None
        
    pos = random.randint(0,num_results-1)
	# checks if valid (only contains ascii characters) and is not a retweet
    if OnlyAscii(search_results[pos].text) and not search_results[pos].retweeted:
        return search_results[pos]
        
    # otherwise removes invalid tweet and searches list again
    else:
        del search_results[pos]
        return findTweet(search_results,num_results-1)

NUM_TWEETS_TO_SEARCH = 50
url = 'https://en.wikipedia.org/wiki/special:random'
response = urllib.request.urlopen(url)

url = response.url
response = urllib.request.urlopen(url)

# "signing into account"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_results = api.search(q="what is", count=NUM_TWEETS_TO_SEARCH)

twt2respond = findTweet(search_results,NUM_TWEETS_TO_SEARCH)
#print(twt2respond.text)

name = twt2respond.user.screen_name
reply = "@"+name+" "+url
twtid = twt2respond.id;
#print(reply)
#print(twtid)

api.update_status(reply, in_reply_to_status_id = twtid)
