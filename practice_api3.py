import pandas as pd
import requests

# get API

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page" : 5
}
response = requests.get(url,params=params)
data = response.json()
df = pd.DataFrame(data)
print(df[["name","current_price"]])