
from src.api.twitter_api import TwitterAPI
from src.utils.logger import Logger
from src.services.ai_ml_component import AILearningComponent
import json

class TweetController:
    def __init__(self, twitter_api: TwitterAPI, logger: Logger, ai_component: AILearningComponent):
        self.twitter_api = twitter_api
        self.logger = logger
        self.ai_component = ai_component

    def stream_tweets(self):
        # Stream tweets using TwitterAPI
        return self.twitter_api.stream_tweets()

    def process_tweet(self, tweet):
        # Process each tweet, apply AI/ML for response generation
        try:
            tweet_data = json.loads(tweet)
            response = self.ai_component.generate_response(tweet_data['content'])
            self.post_tweet(response)
        except Exception as e:
            self.logger.log_error(f"Error in processing tweet: {str(e)}")

    def post_tweet(self, message):
        # Post a tweet using TwitterAPI
        try:
            self.twitter_api.post_tweet(message)
        except Exception as e:
            self.logger.log_error(f"Error in posting tweet: {str(e)}")

