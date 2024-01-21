import nltk
import random
import torch
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from transformers import BertTokenizer, BertModel, GPT2LMHeadModel, GPT2Tokenizer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class AdvancedNLPEngine:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def extract_key_points(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model(input_ids)
        return self.extract_most_important_tokens(outputs, input_ids)

    def extract_most_important_tokens(self, outputs, input_ids):
        last_layer = outputs.last_hidden_state
        attention = torch.sum(last_layer, dim=1)
        top_tokens = torch.argsort(attention, dim=1, descending=True)
        return [self.tokenizer.decode(input_ids[0][idx]) for idx in top_tokens[0][:5]]

class AdvancedResponseGenerator:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def generate_response(self, key_points, user_preferences):
        prompt = self.format_prompt(key_points, user_preferences)
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=50, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def format_prompt(self, key_points, user_preferences):
        prompt_style = user_preferences.get('style', 'friendly')
        prompt = f"{prompt_style} response to: " + ", ".join(key_points) + "."
        return prompt

class UserInteractionManager:
    def __init__(self):
        self.user_preferences = {}
        self.chat_history = {}
        self.key_points_history = {}

    def update_user_preferences(self, user_id, preferences):
        self.user_preferences[user_id] = preferences

    def get_user_preferences(self, user_id):
        return self.user_preferences.get(user_id, {})

    def update_chat_history(self, user_id, response):
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
        self.chat_history[user_id].append(response)

    def remember_key_points(self, user_id, key_points):
        if user_id not in self.key_points_history:
            self.key_points_history[user_id] = []
        self.key_points_history[user_id].extend(key_points)

    def customize_response_style(self, user_id, style_preferences):
        self.update_user_preferences(user_id, {"style": style_preferences})

class Chatbot:
    def __init__(self):
        self.nlp_engine = AdvancedNLPEngine()
        self.response_generator = AdvancedResponseGenerator()
        self.interaction_manager = UserInteractionManager()

    def handle_user_interaction(self, user_id, user_input):
        if user_input.lower() in ['quit', 'exit', 'goodbye']:
            return "Goodbye! If you have more questions, feel free to ask."

        key_points = self.nlp_engine.extract_key_points(user_input)
        user_prefs = self.interaction_manager.get_user_preferences(user_id)
        response = self.response_generator.generate_response(key_points, user_prefs)

        self.interaction_manager.update_chat_history(user_id, response)
        self.interaction_manager.remember_key_points(user_id, key_points)
        return response

class EnhancedChatbot(Chatbot):
    emotion_keywords = {
        "happy": ["happy", "glad", "joy", "excited"],
        "sad": ["sad", "unhappy", "depressed", "down"],
        # Add more as needed
    }

    def analyze_emotion(self, text):
        for emotion, keywords in self.emotion_keywords.items():
            if any(keyword in text.lower() for keyword in keywords):
                return emotion
        return "neutral"

    def handle_user_interaction(self, user_id, user_input):
        emotion = self.analyze_emotion(user_input)
        key_points = self.nlp_engine.extract_key_points(user_input)
        user_prefs = self.interaction_manager.get_user_preferences(user_id)

        # Enhanced response generation with emotion
        response = self.response_generator.generate_response(key_points, user_prefs, emotion)

        self.interaction_manager.update_chat_history(user_id, response)
        self.remember_key_points(user_id, key_points)
        return response

import nltk
import torch
from transformers import BertTokenizer, BertModel, GPT2LMHeadModel, GPT2Tokenizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class AdvancedNLPEngine:
    """
    Advanced NLP engine using BERT for key point extraction.
    """
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def extract_key_points(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model(input_ids)
        return self.extract_most_important_tokens(outputs, input_ids)

    def extract_most_important_tokens(self, outputs, input_ids):
        last_layer = outputs.last_hidden_state
        attention = torch.sum(last_layer, dim=1)
        top_tokens = torch.argsort(attention, dim=1, descending=True)
        return [self.tokenizer.decode(input_ids[0][idx]) for idx in top_tokens[0][:5]]

class AdvancedResponseGenerator:
    """
    Response generator using GPT-2 for creating dynamic responses.
    """
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def generate_response(self, key_points, user_preferences):
        prompt = self.format_prompt(key_points, user_preferences)
        inputs = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=50, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def format_prompt(self, key_points, user_preferences):
        prompt_style = user_preferences.get('style', 'friendly')
        prompt = f"{prompt_style} response to: " + ", ".join(key_points) + "."
        return prompt

class UserInteractionManager:
    """
    Manages user interactions, preferences, and chat history.
    """
    def __init__(self):
        self.user_preferences = {}
        self.chat_history = {}
        self.key_points_history = {}

    def update_user_preferences(self, user_id, preferences):
        self.user_preferences[user_id] = preferences

    def get_user_preferences(self, user_id):
        return self.user_preferences.get(user_id, {})

    def update_chat_history(self, user_id, response):
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
        self.chat_history[user_id].append(response)

    def remember_key_points(self, user_id, key_points):
        if user_id not in self.key_points_history:
            self.key_points_history[user_id] = []
        self.key_points_history[user_id].extend(key_points)

class EnhancedChatbot:
    """
    Enhanced chatbot integrating emotion analysis and advanced NLP.
    """
    emotion_keywords = {
        "happy": ["happy", "glad", "joy", "excited"],
        "sad": ["sad", "unhappy", "depressed", "down"],
    }

    def __init__(self):
        self.nlp_engine = AdvancedNLPEngine()
        self.response_generator = AdvancedResponseGenerator()
        self.interaction_manager = UserInteractionManager()

    def analyze_emotion(self, text):
        for emotion, keywords in self.emotion_keywords.items():
            if any(keyword in text.lower() for keyword in keywords):
                return emotion
        return "neutral"

    def handle_user_interaction(self, user_id, user_input):
        emotion = self.analyze_emotion(user_input)
        key_points = self.nlp_engine.extract_key_points(user_input)
        user_prefs = self.interaction_manager.get_user_preferences(user_id)

        response = self.response_generator.generate_response(key_points, user_prefs, emotion)
        self.interaction_manager.update_chat_history(user_id, response)
        self.interaction_manager.remember_key_points(user_id, key_points)
        return response

# Example usage
chatbot = EnhancedChatbot()
chatbot.interaction_manager.customize_response_style("user123", "informal")
user_input = "Tell me about the latest trends in AI."
response = chatbot.handle_user_interaction("user123", user_input)
print(response)
