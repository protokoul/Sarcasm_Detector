import json

# A text file with one tweet per line

#https://twitter.com/intent/user?user_id=719517296646033409
count = 0

tweets = []
with open('testfile.json', 'r') as file:
	for line in file:
		tweets.append(json.loads(line))
		
print len(tweets)

for tweet in tweets:
	count = count + 1
	print json.dumps(tweet, indent=4)
	print "\n"
