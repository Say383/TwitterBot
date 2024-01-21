import pandas as pd
from textblob import TextBlob

class TweetAnalytics:
    def __init__(self, tweets):
        """
        tweets: List of dictionaries, each dictionary represents a tweet with keys like 'text'.
        """
        self.df = pd.DataFrame(tweets)

    def _calculate_sentiment(self, text):
        """
        Private method to calculate sentiment of a tweet.
        Returns a sentiment label: 'positive', 'negative', or 'neutral'.
        """
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def analyze_sentiments(self):
        """
        Analyzes the sentiments of tweets.
        Returns a DataFrame with original tweets and their sentiment.
        """
        self.df['sentiment'] = self.df['text'].apply(self._calculate_sentiment)
        return self.df

    def keyword_frequency(self, keyword):
        """
        Counts the frequency of a given keyword in tweets.
        keyword: String, the keyword to search for.
        Returns an integer count.
        """
        return self.df[self.df['text'].str.contains(keyword, case=False)].shape[0]
    
    def topic_modeling(self):
        count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')
        doc_term_matrix = count_vect.fit_transform(self.df['text'].values.astype('U'))
        lda = LatentDirichletAllocation(n_components=5, random_state=42)
        lda.fit(doc_term_matrix)
        return lda.components_

    def find_trending_topics(self):
        """
        Identifies trending topics based on hashtags.
        Returns a list of tuples (hashtag, count).
        """
        hashtags = pd.Series(' '.join(self.df['text']).lower().split()).value_counts()
        return hashtags[hashtags.index.str.startswith('#')]

# Example usage
advanced_analytics = AdvancedTweetAnalytics(tweets=[])
topics = advanced_analytics.topic_modeling()