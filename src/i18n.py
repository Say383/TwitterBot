from googletrans import Translator

class Internationalization:
    def __init__(self):
        self.translator = Translator()

    def detect_language(self, text):
        detection = self.translator.detect(text)
        return detection.lang

    def translate_text(self, text, target_language='en'):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

    def respond_in_language(self, message, target_language):
        translated_message = self.translate_text(message, target_language)
        return translated_message

# Example usage
i18n = Internationalization()
detected_language = i18n.detect_language("Hola, ¿cómo estás?")
response = i18n.respond_in_language("Thank you for your message!", detected_language)
