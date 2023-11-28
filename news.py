import requests
import os

BING_URL = "https://api.bing.microsoft.com/v7.0/news/search"


def search_news(name: str) -> list[dict]:
    query = f"{name} news"
    market = "en-US"
    params = {"q": query, "mkt": market}
    headers = {"Ocp-Apim-Subscription-Key": os.environ["BING_API_KEY"]}

    response = requests.get(BING_URL, headers=headers, params=params)

    response.raise_for_status()

    search_results = response.json()

    return [
        {
            "Name": article["name"],
            "Url": article["url"],
            "Description": article["description"],
            "Date Published": article["datePublished"],
        }
        for article in search_results.get("value")
    ][:5]
