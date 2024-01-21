from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

class AILearningComponent:
    def __init__(self):
        self.model = make_pipeline(TfidfVectorizer(), RandomForestClassifier())

    def learn_from_data(self, data):
        features, labels = data
        self.model.fit(features, labels)

    def predict(self, new_data):
        return self.model.predict(new_data)

    def update_model(self, new_data):
        features, labels = new_data
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        accuracy = self.model.score(X_test, y_test)
        return accuracy

# Instance of the Enhanced AI Learning Component
ai_component = AILearningComponent()