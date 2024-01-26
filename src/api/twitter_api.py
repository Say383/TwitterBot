import os
import tweepy
from tweepy import OAuthHandler
from src.utils.logger import Logger
from redis import Redis
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class TwitterAPIError(Exception):
    """Custom exception for Twitter API errors."""
    
class TwitterAPI:
    def __init__(self, logger: Logger):
        consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["POST"],
            backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.api.session.mount("https://", adapter)
        self.logger = logger
        self.cache = Redis(host='localhost', port=6379, db=0, decode_responses=True)

    def _validate_message(self, message):
        if not message or len(message) > 280:
            raise ValueError("Invalid message length")

    def post_tweet(self, message):
        try:
            self._validate_message(message)
            tweet = self.api.update_status(message)
            self.logger.log_info(f"Tweet posted: {message}")
            return tweet
        except tweepy.TweepError as e:
            self.logger.log_error(f"Error posting tweet: {e}")
            raise TwitterAPIError(f"Error posting tweet: {e.api_code}")

    def get_mentions(self, since_id=None):
        cache_key = f"mentions:{since_id}"
        cached_mentions = self.cache.get(cache_key)
        if cached_mentions:
            self.logger.log_info("Fetched mentions from cache")
            return cached_mentions
        try:
            mentions = self.api.mentions_timeline(since_id=since_id)
            self.logger.log_info(f"Fetched {len(mentions)} new mentions")
            self.cache.set(cache_key, mentions, ex=120)  # cache for 2 minutes
            return mentions
        except tweepy.TweepError as e:
            self.logger.log_error(f"Error fetching mentions: {e}")
            raise TwitterAPIError(f"Error fetching mentions: {e.api_code}")

class MyStreamListener(StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False disconnects the stream
            return False
        print(f'Encountered streaming error (status code: {status_code})')
