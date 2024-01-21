
import tweepy
import logging

class TwitterAPI:
    """A wrapper class for interacting with the Twitter API using Tweepy."""

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        """
        Initializes the TwitterAPI with OAuth credentials.
        
        :param consumer_key: Twitter API consumer key
        :param consumer_secret: Twitter API consumer secret
        :param access_token: Twitter API access token
        :param access_token_secret: Twitter API access token secret
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def post_tweet(self, message):
        """
        Posts a tweet to Twitter.

        :param message: The message to be tweeted
        :return: The tweet object or error message
        """
        try:
            tweet = self.api.update_status(message)
            return tweet
        except tweepy.TweepError as e:
            logging.error(f"An error occurred while posting a tweet: {e}")
            return {"error": str(e)}

    def get_mentions(self):
        """
        Retrieves the latest mentions for the authenticated user.

        :return: A list of mention objects or an error message
        """
        try:
            mentions = self.api.mentions_timeline()
            return mentions
        except tweepy.TweepError as e:
            logging.error(f"An error occurred while fetching mentions: {e}")
            return {"error": str(e)}
