from dotenv import load_dotenv
import os
import re
import tweepy
from pocket import Pocket

def main():
    load_dotenv()

    #Twitter keys
    consumer_key = os.environ.get('API_KEY')
    consumer_secret = os.environ.get('API_SECRETKEY')

    #Pocket keys
    p_consumer_key = os.environ.get('POCKET_CONSUMER_KEY')
    p_access_token = os.environ.get('POCKET_ACCESS_TOKEN')

    #authenticate and call twitter api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    p = Pocket(consumer_key=p_consumer_key, access_token=p_access_token)

    #gets JSON of liked tweets
    fav = api.favorites('importhuman', count=100, tweet_mode='extended')

    links = []
    # n = 0
    for status in fav:
        url_list = status['entities']['urls']
        if url_list != []:
            for item in url_list:
                link = item['expanded_url']
                if link not in links:
                    if re.search("//twitter.com/", link) is None:
                        links.append(link)
                        # print(link)
                        p.add(link)
                        # n += 1



if __name__ == "__main__":
    main()
