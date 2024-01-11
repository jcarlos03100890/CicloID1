import tweepy
import pandas as pd
import time

consumer_key = 'cDL4QL1ymg9J5cpAsXrkyMFse'
consumer_secret = '6xSNu2CCCLXYc4rGRZnUvkdRu8Rbmaj9NwAMgu907Wr8gCpVrg'
access_token = '172977303-CnBgGs24r4NyQ9C9dfodtfWJSbsEdwR6yNqFwTfh'
access_token_secret = 'SB2U61qXk3ocxmTOTZeSsXGIgU769ITtetgmOq1bvqbN5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []


def query_to_csv(text_query, count):
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=text_query).items(count)
        tweets_list = [[tweet.id, tweet.created_at, tweet.text] for tweet in tweets]

        # tweet information
        tweets_df = pd.DataFrame(tweets_list, columns=['ID', 'Datetime', 'Text'])

        tweets_df.to_csv('{}-tweets.csv'.format(text_query), sep=',', index=False)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


# X is number of tweets to be retrieved
text_query = 'MODA'
count = 100

query_to_csv(text_query, count)
