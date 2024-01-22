
import tweepy
from tweepy import OAuthHandler, Stream, StreamListener

class TwitterAPI:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def post_tweet(self, message):
        try:
            self.api.update_status(message)
        except tweepy.TweepError as e:
            print(f'Error: {e.reason}')

    def search_tweets(self, query, count=10):
        try:
            return self.api.search(q=query, count=count)
        except tweepy.TweepError as e:
            print(f'Error: {e.reason}')
            return []

class MyStreamListener(StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False disconnects the stream
            return False
        print(f'Encountered streaming error (status code: {status_code})')
