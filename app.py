from dotenv import load_dotenv
load_dotenv()
import os
import tweepy

consumer_key = os.environ.get('API_key')
consumer_secret = os.environ.get('API_secretkey')

#authenticate and call api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# api = tweepy.API(auth)

#prints out JSON of liked tweets 
fav = api.favorites('importhuman', tweet_mode='extended')

links = []
for status in fav:
	if status['entities']['urls'] != []:
		link = status['entities']['urls'][0]['url']
		links.append(link)
		

print(links)


# tweet = api.get_status(1317381768811511808)
# for x in tweet:
# 	print(x)

# print(tweet['entities']['urls'][0]['url'])  gets the link from the tweet

print("done")