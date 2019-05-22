from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/index')
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




def read_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    return content 

def get_movie(src, movie_id):
  movies = read_file(src)
  for movie in movies:
    if movie['id'] == movie_id:
      return movie