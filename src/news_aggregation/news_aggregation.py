import requests

def aggregate_news(sources):
    aggregated_news = []
    for source in sources:
        response = requests.get(source['url'])
        if response.status_code == 200:
            # In a real-world scenario, we would parse the response content
            # and extract the relevant news data.
            news_data = response.json()
            aggregated_news.append(news_data)
        else:
            print(f"Failed to retrieve news from {source['name']}")
    return aggregated_news

# Example usage with mock URLs
sources = [
    {'name': 'Source A', 'url': 'https://api.sourcea.com/news'},
    {'name': 'Source B', 'url': 'https://api.sourceb.com/news'}
]
news = aggregate_news(sources)
print(news)
