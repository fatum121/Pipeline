import pandas as pd

df_csv = pd.read_csv("data/raw/orders.csv")
df_json = pd.read_json("data/raw/customers.json")
print(df_csv.to_string())
print(df_json.to_string())
print(df_csv['date'].drop_duplicates())