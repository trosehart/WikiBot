from bs4 import BeautifulSoup
import re
import urllib.request
import tweepy
import time
import os
from random import seed
from random import random

from PrivateKeys import *

url = 'https://en.wikipedia.org/wiki/Main_Page'
cur_dir = os.getcwd()

seed(1)
ran_int = int(random()*1000000)
image_name = str(ran_int) + ".jpg"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response,'html.parser')

#finds what is within the <div id=mp-dyk> tag
div_mp_dyk = soup.find("div", {"id": "mp-dyk"})

#array to store strings of facts
factArray = []

#loops through the <div id=mp-dyk> tag, finding everything with <li> tags
for tag in div_mp_dyk.find_all('li'):
    #prints the tag content
	#print(tag.text)
	
	#adds string to array if it contains "that", which shows it is a fact
	if 'that' in tag.text:
		factArray.append("Did you know " + tag.text[4:])
	
#for fact in factArray:
#	print(fact)


#downloads image
images = soup.find_all('img', {'src':re.compile('.jpg')})
imurl = "h"
for image in images: 
	#to get image for specific fact, as long as it is the first with "mp-dyk" id in tag
	if [p.get('id') for p in image.findAllPrevious(id='mp-dyk')]:
		if imurl == "h":
			imurl = "https:"+image['src']
			pos = imurl.find('jpg');
			imurl = imurl[0:pos+3]
			imurl = imurl.replace('thumb/','')
			#print(imurl)
	#print(image['src']+'\n')
	#if imurl == "h":
	#	imurl = "https:"+image['src']
	
#print(imurl)

f = open(image_name,'wb')
f.write(urllib.request.urlopen(imurl).read())
f.close()

image = open(cur_dir + '/' + image_name,'rb')



'''
#have to fill this in with your info
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = '' 
'''

#"signing into account"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#posting facts to Twitter
for fact in factArray:  
	if "pictured" in fact or "portrait shown" in fact or "depicted" in fact:
		#print(fact)
		api.update_with_media(media=image, status=fact, filename=image_name)

	else:
		#print(fact)
		api.update_status(fact)
	time.sleep(2)

time.sleep(5)
os.remove(image_name)
