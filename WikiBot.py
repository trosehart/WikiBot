from bs4 import BeautifulSoup
import urllib.request
import tweepy

#function to find facts
def findFact():
	response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
	html = response.read()
	
	factArray = []
	
	
	#have to parse website for wikipedia's facts, trying to use BeautifulSoup
	newFact = ""
	
	#adding next fact to array of facts
	factArray.append(newFact)
	
	return factArray
	
	
	
	
#print(html)

#just testing
for a in range(10):
	print(a)
"""
#have to fill this in with my info
consumer_key = ''
consumer_token = ''
access_token = ''
access_token_secret = '' 

#"signing into account"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#posting facts to Twitter
for fact in factArray:  
    api.update_with_media(fact)
    time.sleep(200)
"""