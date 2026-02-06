import pandas as pd
import requests

df = pd.read_csv("data.csv")
print(df)

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
    }

response = requests.get(url, params=params)
print(response.status_code)

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
     "vs_currency": "usd",
     "order": "market_cap_desc",
     "per_page": 5,
     "page": 1
}

response = requests.get(url,params=params)

print(response.status_code)

data = response.json()

df = pd.DataFrame(data)

print(df[["id","symbol","current_price"]].head())


url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
     "vs_currency": "usd",
     "order": "market_cap_desc",
     "per_page": 5,
     "page": 1
}

response = requests.get(url,params=params)

print(response.status_code)

data = (response.json())

df = pd.DataFrame(data)

print(df.sort_values("market_cap",ascending=False)[["name","symbol","market_cap"]])