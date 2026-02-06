import pandas as pd 
import requests

url = "http://universities.hipolabs.com/search"

params = {
    "country": "Pakistan"
}

response = requests.get(url,params=params)

print(response.status_code)

data = response.json()

df = pd.DataFrame(data)

print(df[["name","country","domains"]].head(10))