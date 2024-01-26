def post_to_social_media(platform, message):
    # In a real implementation, you would use the API of the social media platform.
    # Below is a mock example.
    if platform.lower() == 'twitter':
        # Use Twitter's API to post the message.
        print("Posting to Twitter: " + message)
    elif platform.lower() == 'facebook':
        # Use Facebook's API to post the message.
        print("Posting to Facebook: " + message)
    else:
        print("Unsupported platform.")

post_to_social_media('twitter', 'Hello, World!')  # Example usage
