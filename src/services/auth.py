
from flask_oauthlib.client import OAuth

class TwitterAuth:
    def __init__(self, app, api_key, api_secret):
        self.oauth = OAuth(app)
        self.twitter = self.oauth.remote_app(
            'twitter',
            consumer_key=api_key,
            consumer_secret=api_secret,
            request_token_params={'scope': 'email'},
            base_url='https://api.twitter.com/1.1/',
            request_token_url=None,
            access_token_url='/oauth/access_token',
            authorize_url='https://api.twitter.com/oauth/authorize',
            access_token_method='POST'
        )

    def authorize(self):
        return self.twitter.authorize(callback=url_for('authorized', _external=True))

    def authorized(self, resp):
        if resp is None or resp.get('oauth_token') is None:
            return 'Access denied: reason={} error={}'.format(
                request.args['error_reason'],
                request.args['error_description']
            )
        session['twitter_token'] = (resp['oauth_token'], resp['oauth_token_secret'])
        return 'You were signed in as {}'.format(resp['screen_name'])
