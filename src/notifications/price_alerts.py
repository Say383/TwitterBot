
import requests
import time

# Function to get the current price of a cryptocurrency
def get_current_price(coin_id):
    try:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json().get(coin_id, {}).get('usd', 0)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price for {coin_id}: {e}")
        return None

# Function to check and alert if the price reaches the target
def check_and_alert(coin_id, target_price):
    current_price = get_current_price(coin_id)
    if current_price is None:
        return  # Skip this iteration if there was an error fetching the price
    
    if current_price >= target_price:
        print(f"Alert: {coin_id.capitalize()} has reached the target price of ${target_price}! Current price: ${current_price}")
    else:
        print(f"{coin_id.capitalize()} is below the target price of ${target_price}. Current price: ${current_price}")

# Example cryptocurrency targets
cryptocurrency_targets = {
    'bitcoin': 50000,
    'ethereum': 3000,
    'litecoin': 200
}

# Main loop to check prices periodically
while True:
    for coin_id, target_price in cryptocurrency_targets.items():
        check_and_alert(coin_id, target_price)
    
    # Pause for a specified time interval (e.g., 5 minutes)
    time.sleep(300)
