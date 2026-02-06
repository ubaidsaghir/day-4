import pandas as pd
import requests

url = "https://api.open-meteo.com/v1/forecast"

params ={
    "latitude": 24.8607,
    "longitude": 67.0011,
    "current_weather": True
}

response = requests.get(url,params=params)

print(response.status_code)
data = response.json()

weather = data["current_weather"]



df = pd.DataFrame([weather])

print(df[["temperature","windspeed"]].head(10))