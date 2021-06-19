import tweepy
import pandas as pd
import csv

# Twitter Developer keys here
# It is CENSORED
consumer_key = ''
consumer_key_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth , wait_on_rate_limit=True)

df = pd.read_csv('24.csv')

#print(df.head())

tweet_id = df['tweet_id'].to_list()
type(tweet_id[0])

tweet_id = df['tweet_id'].to_list()


tweets =[]
ijk = 1
for tweet in tweet_id:
    print (ijk)
    ijk = ijk + 1
    try:
        tweetFetched = api.get_status(tweet)
        #print("Tweet fetched" + tweetFetched.text)
        tweetFetched.text = tweetFetched.text.replace('\n' , ' ' ).replace('\r', '')
        print(tweetFetched.text)
        tweets.append(tweetFetched.text)
 #       print(tweets)

    except:
#        tweets.append(['noValue' , "Hate"])
        print("in except")

        continue
print(tweets)


import pandas as pd
df = pd.DataFrame(tweets)
df.to_csv('24tweet.csv', index=False)

