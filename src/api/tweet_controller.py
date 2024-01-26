from src.api.twitter_api import TwitterAPI
from src.utils.logger import Logger

class TweetController:
    def __init__(self, config, logger, ai_component):
        twitter_api_config = {
            "api_key": config["api_key"],
            "api_secret_key": config["api_secret_key"],
            "access_token": config["access_token"],
            "access_token_secret": config["access_token_secret"]
        }
        self.twitter_api = TwitterAPI(twitter_api_config)
        self.logger = logger
        self.ai_component = ai_component

    def listen_for_tweets(self):
        # Fetch new tweets from TwitterAPI
        return self.twitter_api.get_new_tweets()

    def process_tweet_data(self, data):
        # Process incoming tweet data, and prepare response
        return self.ai_component.prepare_response(data)

    def post_tweet(self, message):
        # Code to post a tweet using the Twitter API
        try:
            self.twitter_api.post_tweet(message)
        except Exception as e:
            self.logger.log_error(f"Error posting tweet: {str(e)}")

    # Additional methods can be added here for more functionality
