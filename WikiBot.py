from bs4 import BeautifulSoup
import re
import urllib.request
import tweepy
import time
import os
from random import seed
from random import random

from PrivateKeys import *
#
#
# TODO: Make this code less garbage, functions and stuff
#
#
url = 'https://en.wikipedia.org/wiki/Main_Page'
cur_dir = os.getcwd()

seed()
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
    #adds string to array if it contains "that", which shows it is a fact
    if 'that' in tag.text:
        factArray.append("Did you know " + tag.text[4:])


#find URL for image
images = soup.find('div', {'class':'dyk-img'})
image = images.find('img')
imurl = "https:"+image['src']
if 'svg' not in imurl:
    imurl = imurl.rsplit('/', 1)[0]
    imurl = imurl.replace('thumb/','')

# TODO: this needs to be fixed, this try/except should just be temporary
try:
    if ".webm" not in imurl:
        #downloads image
        f = open(image_name,'wb')
        f.write(urllib.request.urlopen(imurl).read())
        f.close()

        image = open(cur_dir + '/' + image_name,'rb')

    else:
        image = None

except:
    image = None

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
    if "pictured" in fact or "portrait shown" in fact or "depicted" in fact or "shown)" in fact:
        try:
            api.update_with_media(media=image, status=fact, filename=image_name)
        
        except:
            print("Image unable to be posted - " + imurl)

    else:
        api.update_status(fact)
    time.sleep(2)

time.sleep(5)
os.remove(image_name)
