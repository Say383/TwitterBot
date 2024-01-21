
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

class NLPProcessor:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stop_words = set(stopwords.words('english'))

    def analyze_sentiment(self, text):
        return self.sia.polarity_scores(text)

    def extract_keywords(self, text):
        word_tokens = word_tokenize(text)
        keywords = [word for word in word_tokens if word not in self.stop_words and word.isalpha()]
        return keywords

    def determine_response(self, text):
        sentiment_score = self.analyze_sentiment(text)
        keywords = self.extract_keywords(text)

        # Example response logic based on sentiment and keywords
        if sentiment_score['compound'] > 0.5:
            return 'Positive sentiment detected.'
        elif sentiment_score['compound'] < -0.5:
            return 'Negative sentiment detected.'
        else:
            return f'Neutral sentiment. Keywords: {", ".join(keywords)}'
