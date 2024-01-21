import unittest
from twitter_api import TwitterAPI
from analytics import TweetAnalytics
from community import CommunityManager

class TwitterBotTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
        cls.analytics = TweetAnalytics(tweets=[])
        cls.community_manager = CommunityManager()

    def test_tweet_posting(self):
        tweet = self.twitter_api.post_tweet("Test tweet")
        self.assertIsNotNone(tweet)

    def test_sentiment_analysis(self):
        sentiments = self.analytics.analyze_sentiments([{'text': 'Happy coding!'}])
        self.assertIn('positive', sentiments['sentiment'].values)

    def test_community_response(self):
        response = self.community_manager.respond_to_user_message("Hello bot!")
        self.assertIsNotNone(response)
        self.assertIn("Thank you", response)

if __name__ == '__main__':
    unittest.main()
