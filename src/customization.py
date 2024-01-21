class BotCustomization:
    def __init__(self):
        self.settings = {
            "response_style": "friendly",
            "interaction_frequency": "normal",
            "content_preference": "general"
        }

    def update_settings(self, new_settings):
        self.settings.update(new_settings)
        return "Bot settings updated."

    def get_response_style(self):
        return self.settings["response_style"]

    def get_interaction_frequency(self):
        return self.settings["interaction_frequency"]

    def customize_content(self, content):
        if self.settings["content_preference"] == "tech":
            return f"Tech News: {content}"
        else:
            return f"General News: {content}"

# Example usage
bot_customization = BotCustomization()
bot_customization.update_settings({"content_preference": "tech"})
response_style = bot_customization.get_response_style()
content = bot_customization.customize_content("Latest trends in AI")
