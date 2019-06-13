#%%
import pandas as pd
import numpy as np
import matplotlib
import datetime
from matplotlib import pyplot as plt
import os
 
def load_csv_data(path):
  return pd.read_csv(path)

def load_json_data(path):
  return pd.read_json(path)

#%%

def draw_count_by_districts():
  df = load_csv_data('metro-bike-share-trip-data.csv')
  dist = df['Council Districts'].groupby(df['Council Districts']).count()
  return dist

df = draw_count_by_districts()
df
#%%
