import tweepy 
import io
import json
import os
from time import gmtime, strftime


############### READ HERE ###########################

###### SCROLL DOWN AT THE BOTTOM, ENTER THE TWITTER HANDLE YOU WANT TO EXTRACT IN A VARIABLE #####

############### READ ABOVE LINES ###########################











#Twitter API credentials
consumer_key = 'Ma9AEJaAT4cMM1uEQgnPXpr2c'
consumer_secret = 'QExQVza6xDNSEIA4cB0qoYY71qHpRimMinkqhcUdhg8T5Q71z1'
access_key = '151505107-3vnvcOopKVf6mMPLwdTtWovlmBa0j7w8uoP9Oa5H'
access_secret = '8zPLJLFkrq9fUYzhsSHPuGwO1GyhReIaPWxKUMr7UYCc2'


def generateFilename(screen_name):
	#path = "/home/abhishek/Desktop/twitter_machine/Test/JsonTweets"
	path = str(os.getcwd())+"/JsonTweets"
	name = strftime("%Y-%m-%d-%H:%M:%S",gmtime())

	#Checks of the directory exists or not
	if not os.path.isdir(path):
		os.makedirs(path)

	filename = path + "/" + str(name) + "-" + screen_name + ".json"
	return filename

#write to json file	
def writeTweetToFile(tweet_stream, screen_name):
	OUT_FILE = generateFilename(screen_name)
	with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
		for status_tweet in tweet_stream:
			tweet = status_tweet._json

			if tweet['text'].startswith("RT") == False and tweet['retweeted'] == False:
				if tweet['in_reply_to_screen_name'] is None:
					if not tweet['truncated']:
						if not 'media' in tweet['entities']:
							if not tweet['entities']['urls']:
								'''
									if Python 2 then use:
										f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
									else:
										f.write(str(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))		
								'''
								#f.write(str(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
								f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
								print(tweet['text'])
			else:
				print("########## BREAKING UP ##########")
				if os.path.isfile(OUT_FILE):
					if os.path.getsize(OUT_FILE) == 0:
						os.remove(OUT_FILE)
						print("Empty file was removed !!!")
				break

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the incoming Tweets
	returned_tweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	stream = api.user_timeline(screen_name = screen_name,count=200)
	
	writeTweetToFile(stream, screen_name)
	#save most recent tweets
	returned_tweets.extend(stream)

	#save the id of the oldest tweet less one
	oldest = returned_tweets[-1].id - 1


	while len(stream) > 0:
		#all subsiquent requests use the max_id param to prevent duplicates
		stream = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		writeTweetToFile(stream, screen_name)
		#save most recent tweets
		returned_tweets.extend(stream)

		#save the id of the oldest tweet less one
		oldest = returned_tweets[-1].id - 1
			






###### Enter the twitter handle without @
###### example: @RetardsIncorp is written as below

username = "sarcastweet"
get_all_tweets(username)