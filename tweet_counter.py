import json
import pandas as pd
import os


path = str(os.getcwd())+"/JsonTweets"
count = 0

def fetchTweetCount(filename):
	global path,count

	fname = path + "/" + filename

	if os.path.getsize(fname) == 0:
		os.remove(fname)
	else:
		with open(fname, 'r') as file:
			for line in file:
				count = count + 1


def main():
	global path,count
	files = os.listdir(path)
	noTweets = True

	if files == []:
		print("Json Folder is empty. Try Fetching some tweets first")
	else:
		noTweets = False
		for file in files:
			input_file = str(file)
			fetchTweetCount(input_file)
		print(count)
	


main()