import tweepy
import config
import pandas as pd
client = tweepy.Client(bearer_token=config.BEARER_TOKEN, access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)

query = 'kinerja kepolisian OR kinerja polisi OR kinerja polri OR #kinerjapolisi -is:retweet lang:id'

file_name = 'Dataset_Kinerja_polisi.txt'

tweets = tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=[
                         'created_at'], max_results=100).flatten(limit=500)
#menggunakan csv
# df = pd.DataFrame(tweets)
# df.to_csv(file_name, encoding= 'utf-8', columns=['id', 'created_at', 'text'])

#menggunakan txt
with open(file_name, 'a', encoding='utf-8') as f:

    for count, tweet in enumerate(tweets):
        created_time = tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        f.write(
            f' id: {tweet.id}, \n time: {created_time}, \n text: {tweet.text}\n\n')

