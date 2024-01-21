
import requests

def get_coin_data(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
if __name__ == '__main__':
    coin_id = 'bitcoin'  # Example coin ID
    data = get_coin_data(coin_id)
    if data:
        print(f"Coin: {data['name']}")
        print(f"Current Price: {data['market_data']['current_price']['usd']} USD")
