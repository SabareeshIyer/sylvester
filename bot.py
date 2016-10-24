'''
Bot using Tweepy to access Twitter API and get 3 recent tweets about a particular hastag and retweet those with
comment where the comment text is text generated from Markov chain created from a given corpus text.
Libraries used: tweepy, markovify
Resources: Alice In Wonderland by Lewis Carrol (as feeder text)
Hashtag: #AliceInWonderland
'''



import tweepy, time
import markovify
from credentials import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


with open("Alice_In_Wonderland.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

tweetlist = [None] * 3

#Three randomly-generated sentences of no more than 80 characters
for i in range(3):
    tweetlist[i] = (text_model.make_short_sentence(80))


results = api.search('%23AliceInWonderland',languages=["en"],show_user = True)
c = 0
for result in results:
	
	if(c>2):
		break
	tw_url = 'http://twitter.com/'+result.user.screen_name+'/status/'+str(result.id)
	tweet_text = '#markovbot '+tweetlist[c]+ ' #AliceInWonderland '+ tw_url
	c = c+1
	print(tweet_text)
	api.update_status(status=tweet_text)
	time.sleep(10) # Sleep for 10 seconds

#print 	('All done!')