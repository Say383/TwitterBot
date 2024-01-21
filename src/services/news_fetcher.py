
import requests

class NewsFetcher:
    def __init__(self, api_endpoint, api_key):
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def fetch_news(self, query_params):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = requests.get(self.api_endpoint, params=query_params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            # Handle specific HTTP errors as needed
        except Exception as err:
            print(f'An error occurred: {err}')
            # Handle other errors like connection errors, timeouts, etc.
        return None
