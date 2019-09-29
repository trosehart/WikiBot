from bs4 import BeautifulSoup
import re
import urllib.request
import urllib
import tweepy

	
url = 'https://en.wikipedia.org/wiki/Main_Page'

#just testing
#for a in range(10):
#	print(a)

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
		factArray.append(("Did you know " + tag.text[4:])[0:139])
	
for fact in factArray:
	print(fact)
	


#downloads image
images = soup.find_all('img', {'src':re.compile('.jpg')})
imurl = "h"
for image in images: 
	#print(image['src']+'\n')
	if imurl == "h":
		imurl = "https:"+image['src']
	
print(imurl)
f = open('1.jpg','wb')
f.write(urllib.request.urlopen(imurl).read())
f.close()

image = open('1.jpg','rb')



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
	if "pictured" in fact:
		api.update_with_media(image, status=fact)
	else:
		api.update_with_media(status=fact)
		
    time.sleep(200)
"""