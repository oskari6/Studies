import requests
import pprint

def get_price(symbol):

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    parameters = {
        "symbol": symbol
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "29cb6142-265e-4850-acf0-6f7c05803c3f"
    }

    response = requests.get(url, params=parameters, headers=headers)

    return response.json().get("data", {}).get("BTC", {}).get(
        "quote", {}).get("USD", {}).get("price", {})

response = input("give me a cryptocurrency ticker: ")
print(get_price(response))