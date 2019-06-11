
#%%
import pandas as pd 

def load_data(file):
  return pd.read_json(file, orient='split')

laptop_alza_df = load_data('laptop_alza.json')

laptop_amazon_df = load_data('laptop_from_amazon.json')

print(laptop_alza_df)

print(laptop_amazon_df)