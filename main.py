import time
import tweepy
import traceback
import logging


api = tweepy.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,access_token=ACCESS_KEY,access_token_secret=ACCESS_SECRET)


alreadymentioned = []
##mentions = api.search_recent_tweets(query=query, max_results=10)
while True:
    mentions = api.get_users_mentions(id=1472630658652676103)

    try:
        for index, mention in enumerate(mentions.data):
            if index == 0 and mention not in alreadymentioned:
                alreadymentioned.append(mention)
                print(mention)
                whoami = str(mention.id)
                api.create_tweet(in_reply_to_tweet_id=whoami, text="TEST")


    except Exception as e:
        logging.error(traceback.format_exc())
    time.sleep(30)
