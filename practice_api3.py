import pandas as pd
import requests

# get API

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "cad",
    "per_page" : 10
}
response = requests.get(url,params=params) 
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad+per_page=10
data = response.json()
df = pd.DataFrame(data)
print(df[["name","current_price"]])

