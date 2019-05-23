from flask import Flask, render_template, jsonify, request, make_response, redirect, url_for
import json

API_KEY = 'bwqMA2tksVHWx4e0Fbx36R1UTSsW0LKN'

app = Flask(__name__)

@app.route('/movies')
def index():
  movie_data = read_file('./data/movie.json')
  return render_template('index.html', movies = movie_data)

@app.route('/movies/<movie_id>')
def movie(movie_id):
  movie = get_movie('./data/movie.json', movie_id)
  if movie:
    return render_template('movie.html', movie = movie)
  else:
    return render_template('not_found.html')

@app.route('/movies/add-movie')
def add_movie():
  return render_template('add_movie.html')

@app.route('/movies/edit-movie/<movie_id>')
def edit_movie(movie_id):
  movie = get_movie('./data/movie.json', movie_id)
  if movie:
    return render_template('edit_movie.html', movie = movie)
  else:
    return render_template('not_found.html')


@app.route('/api/movies')
def api_get_all_movies():
  movie_data = read_file('./data/movie.json')
  return jsonify(movie_data)

@app.route('/api/movies/<movie_id>')
def api_get_movie_by_id(movie_id):
  movie = get_movie('./data/movie.json', movie_id)
  return jsonify(movie)

@app.route('/api/movies', methods=['POST'])
def api_post_movie():
  x_api_key = request.form['x-api-key']
  response = verify_api_key(request, x_api_key)
  if response:
    return response
  movie_data = read_file('./data/movie.json')
  movie = {
    'id': str(len(movie_data) + 1), 
    'title': request.form['title'],
    'year': request.form['year'],
    'genres': request.form['genres'],
    'image': request.form['title'],
    'summary': request.form['summary']
    }
  movie_data.append(movie)
  # movies = request.get_json('data')
  # for index in range(len(movies)):
  #   movies[index]['id'] = str(len(movie_data) + 1)
  #   movie_data.append(movies[index])
  write_to_file('./data/movie.json', movie_data)
  # return make_response(jsonify('status: Success'), 200)
  return redirect(url_for('index'))

# @app.route('/api/movies/<movie_id>', methods=['PUT'])
@app.route('/api/movies/edit/<movie_id>', methods=['POST'])
def api_put_movie(movie_id):
  x_api_key = request.form['x-api-key']
  
  response = verify_api_key(request, x_api_key)
  if response:
    return response

  movie_data = read_file('./data/movie.json')
  [response, target_index] = is_movie_existing(movie_data, movie_id)
  if response:
    return response
  
  # movie_info = request.get_json('data')[0]
  movie_info = {
    'id': movie_id, 
    'title': request.form['title'],
    'year': request.form['year'],
    'genres': request.form['genres'],
    'image': request.form['title'],
    'summary': request.form['summary']
    }

  for key, item in movie_info.items():
    movie_data[target_index][key] = item
  movie_data[target_index]['id'] = movie_id
  write_to_file('./data/movie.json', movie_data)
  # return make_response(jsonify('status: Success'), 200)
  return redirect(url_for('index'))



@app.route('/api/movies/<movie_id>', methods=['DELETE'])
def api_delete_movie(movie_id):
  x_api_key = request.form['x-api-key']
  response = verify_api_key(request, x_api_key)
  if response:
    return response

  movie_data = read_file('./data/movie.json')
  [response, target_index] = is_movie_existing(movie_data, movie_id)
  if response:
    return response
  movie_data.pop(target_index)
  write_to_file('./data/movie.json', movie_data)
  return make_response(jsonify('status: Success'), 200)



def verify_api_key(request, key):
  if API_KEY != request.headers.get('x-api-key') and API_KEY != key:
    return make_response(jsonify({'error': 'Invalid API_KEY'}), 403)
  return None

def is_movie_existing(movie_data, movie_id):
  target_index = None
  response = None
  for index in range(len(movie_data)):
    if movie_data[index]['id'] == movie_id:
      target_index = index
  if target_index == None:
    response = make_response(jsonify({'error': f'No movie found with {movie_id} ID'}), 404)
  return [response, target_index]


def read_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    return content 

def write_to_file(des_file, data):
  with open(des_file, 'w') as out_file:
    json.dump(data, out_file)

def get_movie(src, movie_id):
  movies = read_file(src)
  for movie in movies:
    if movie['id'] == movie_id:
      return movie
  return None
