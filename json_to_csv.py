import json
import pandas as pd
import os


#path = "/home/abhishek/Desktop/twitter_machine/Test/JsonTweets"
path = str(os.getcwd())+"/JsonTweets"
df = pd.DataFrame(columns = ['Text','Language', 'Country'])

def fetchTweets(filename):
	global path,df

	tweets = []
	texts = []
	tweet_language = []
	tweet_country = []
	fname = path + "/" + filename

	with open(fname, 'r') as file:
		for line in file:
			try:
				tweets.append(json.loads(line))
			except Exception as e:
				print(e)

		for tweet in tweets:
			try:
				texts.append(tweet['text'])
				tweet_language.append(tweet['lang'])
				if tweet['place'] != None:
					tweet_country.append(tweet['place']['country'])
				else:
					tweet_country.append(None)
			except Exception as e:
				print(e)

		tweet_info = zip(texts, tweet_language, tweet_country)
		for text, language, country in tweet_info:
			try:
				df = df.append({'Text':text,
								'Language':language,
								'Country':country}, ignore_index = True)
			except Exception as e:
				print(e)


def main():
	global path,df
	files = os.listdir(path)
	noTweets = True

	if files == []:
		print("Json Folder is empty. Try Fetching some tweets first")
	else:
		noTweets = False
		for file in files:
			input_file = str(file)
			fetchTweets(input_file)
	
	try:
		if not noTweets:
			save = str("mobile.csv")
			df.to_csv(save)	
	except Exception as e:
		print(e)


#main()