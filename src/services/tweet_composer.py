
class TweetComposer:
    MAX_TWEET_LENGTH = 280  # Twitter's character limit

    def __init__(self, content_source):
        self.content_source = content_source

    def compose_tweet(self):
        content = self.content_source.get_content()
        tweet = self._truncate_content(content)
        return tweet

    def _truncate_content(self, content):
        if len(content) <= self.MAX_TWEET_LENGTH:
            return content
        else:
            # Truncate content to fit within the character limit
            return content[:self.MAX_TWEET_LENGTH - 3] + '...'

# Example usage
# content_source = SomeContentSource()  # This could be a news service, quote generator, etc.
# composer = TweetComposer(content_source)
# tweet = composer.compose_tweet()
