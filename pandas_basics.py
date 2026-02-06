import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print(df.describe())

print(df.shape)

print(df)

print(df.iloc[1])