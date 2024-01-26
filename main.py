import os
import random
from textblob import TextBlob
from tweepy import OAuthHandler, API
from dotenv import load_dotenv
from src.utils.logger import Logger
from datetime import datetime

# Load environment variables
load_dotenv()

# Twitter API authentication
auth = OAuthHandler(
    os.getenv('TWITTER_CONSUMER_KEY'),
    os.getenv('TWITTER_CONSUMER_SECRET'))
auth.set_access_token(
    os.getenv('TWITTER_ACCESS_TOKEN'),
    os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
api = API(auth)

# Initialize Logger
logger = Logger()

class ResponseFactory:
    def __init__(self):
        self.promotional_messages = [
            "FlorkyCoin to the moon! 🚀 #FlorkyCoin",
            "Don't miss out on the next big thing in crypto - FlorkyCoin. 💰",
            "Join the FlorkyCoin revolution today and be a part of the future. 🔮",
        ]
    
    def create_response(self, tweet_text):
        sentiment = self.analyze_sentiment(tweet_text)
        if 'FlorkyCoin' in tweet_text.lower():
            return random.choice(self.promotional_messages)
        return self.generate_humorous_response(sentiment, tweet_text)

    def analyze_sentiment(self, tweet_text):
        analysis = TextBlob(tweet_text)
        return analysis.sentiment

    def generate_humorous_response(self, sentiment, tweet_text):
        positive_templates = [
            "We're just as thrilled as you are! But can you be as cool as FlorkyCoin? Doubt it. 😉",
            "We're all smiles here, just like when we look at FlorkyCoin's performance. 😄",
        ]
        negative_templates = [
            "Feeling down? Maybe you need more FlorkyCoin in your life. It's scientifically unproven to cure sadness!",
            "If your day's as bad as you say, it's time to switch to FlorkyCoin and turn that frown upside down. 😏",
        ]
        neutral_templates = [
            "We see your point, but have you considered adding a sprinkle of FlorkyCoin to spice things up?",
            "We're not sure if we should laugh or cry, but we'll settle for buying more FlorkyCoin!",
        ]

        if sentiment.polarity > 0.1:
            return random.choice(positive_templates)
        elif sentiment.polarity < -0.1:
            return random.choice(negative_templates)
        else:
            return random.choice(neutral_templates)

class TweetController:
    def __init__(self, api, logger):
        self.api = api
        self.logger = logger
        self.response_factory = ResponseFactory()

    def post_tweet(self, message, reply_to_id=None):
        try:
            self.api.update_status(message, in_reply_to_status_id=reply_to_id)
            self.logger.log_info(f"Tweet posted: {message}")
        except Exception as e:
            self.logger.log_error(str(e))

    def handle_tweet(self, tweet_id, tweet_text):
        response = self.response_factory.create_response(tweet_text)
        self.post_tweet(response, reply_to_id=tweet_id)

def start_bot():
    tweet_controller = TweetController(api, logger)
    while True:
        try:
            tweet_id, tweet_text = listen_for_tweets_and_requests()
            tweet_controller.handle_tweet(tweet_id, tweet_text)
            log_interaction(tweet_id, response)
        except Exception as e:
            logger.log_error(str(e))

def listen_for_tweets_and_requests():
    new_tweet = api.mentions_timeline(count=1)[0]
    return new_tweet.id_str, new_tweet.text

def log_interaction(tweet_id, response, username):
    with open('bot_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.now()}: Responded to tweet ID {tweet_id} "
                       f"from user {username} with message: {response}\n")def log_interaction(tweet_id, response):
    
if __name__ == '__main__':
    start_bot()
