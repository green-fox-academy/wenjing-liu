#%%
import pandas as pd
import json
import numpy as np 
import seaborn

#%%
def load_movies(path):
  movies = pd.read_csv(path, parse_dates=['release_date'])
  json_columns = ['genres', 'keywords', 'production_countries', 'production_companies', 'spoken_languages']
  for column in json_columns:
    movies[column] = movies[column].apply(json.loads)
  return movies

def load_credits(path):
  credits = pd.read_csv(path)
  json_columns = ['cast', 'crew']
  for column in json_columns:
    credits[column] = credits[column].apply(json.loads)
  return credits

#%%
def merge_data(credits, movies):
  merge_data = pd.merge(credits, movies, left_on='movie_id',right_on='id', how='outer', suffixes=('', '_y'))
  merge_data.drop(list(merge_data.filter(regex='_y$')), axis=1, inplace=True)
  return merge_data

#%%
TMDB_TO_IMDB_SIMPLE_EQUIVALENCIES = {
  'budget': 'budget',
  'genres': 'genres',
  'revenue': 'gross',
  'title': 'movie_title',
  'runtime': 'duration',
  'original_language': 'language',
  'keywords': 'plot_keywords',
  'vote_count': 'num_voted_users',
}

IMDB_COLUMNS_TO_REMAP = {'imdb_score': 'vote_average'}

def safe_access(container, index_values):
  # return missing value rather than an error upon indexing/key failure
  result = container
  try:
    for idx in index_values:
      result = result[idx]
    return result
  except IndexError or KeyError:
    return pd.np.nan

def get_crew_by_job(crew_data, job_descriptor, attr):
  workers = [x[attr] for x in crew_data if x['job'] == job_descriptor]
  return safe_access(workers, [0])

def pipe_flatten_names(keywords):
  return '|'.join(x['name'] for x in keywords)

def convert_format(data):
  data.rename(columns=TMDB_TO_IMDB_SIMPLE_EQUIVALENCIES, inplace=True)
  data['title_year'] = pd.to_datetime(data['release_date']).apply(lambda x: x.year)
  data['title_month'] = pd.to_datetime(data['release_date']).apply(lambda x: x.month)
  data['language'] = data['spoken_languages'].apply(lambda x: safe_access(x, [0, 'name']))
  data['country'] = data['production_countries'].apply(lambda x: safe_access(x, [0, 'name']))
  data['director_name'] = data['crew'].apply(lambda x: get_crew_by_job(x, 'Director', 'name'))
  data['director_gender'] = data['crew'].apply(lambda x: get_crew_by_job(x, 'Director', 'gender'))
  data['actor_1_name'] = data['cast'].apply(lambda x: safe_access(x, [1, 'name']))
  data['actor_1_gender'] = data['cast'].apply(lambda x: safe_access(x, [1, 'gender']))
  data['actor_2_name'] = data['cast'].apply(lambda x: safe_access(x, [2, 'name']))
  data['actor_2_gender'] = data['cast'].apply(lambda x: safe_access(x, [2, 'gender']))
  data['actor_3_name'] = data['cast'].apply(lambda x: safe_access(x, [3, 'name']))
  data['actor_3_gender'] = data['cast'].apply(lambda x: safe_access(x, [3, 'gender']))
  data['genres'] = data['genres'].apply(pipe_flatten_names)
  data['plot_keywords'] = data['plot_keywords'].apply(pipe_flatten_names)
  data.drop(['crew', 'cast', 'production_countries', 'production_companies', 'id', 'original_title', 'release_date'], axis=1, inplace=True)
  return data

#%%
def get_data():
  credits = load_credits('credits.csv')
  movies = load_movies('movies.csv')
  merged_df = merge_data(credits, movies)
  data = convert_format(merged_df)
  return data


#%%

def show_missing_columns(data):
  missing_df = data.isnull().sum(axis=0).reset_index()
  missing_df.columns = ['column_name', 'missing_count']
  missing_df['filling_factor'] = (data.shape[0] - missing_df['missing_count']) / data.shape[0] * 100
  return missing_df.sort_values('filling_factor').reset_index(drop = True)


data = get_data()
show_missing_columns(data)
# https://www.kaggle.com/sohier/film-recommendation-engine-converted-to-use-tmdb


#%%
