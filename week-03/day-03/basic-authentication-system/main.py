from flask import Flask, render_template, redirect, url_for, request
import json
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
  error = None
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    users = read_file('./data/user.json')
    is_already_exist = False
    for user in users:
      if user['username'] == username:
        error = 'username already existing'
        is_already_exist = True
        break
      elif user['email'] == email:
        error = 'email already existing'
        is_already_exist = True
        break
    if not is_already_exist:
      users.append({'username': username, 'email': email, 'password': password})
      write_to_file('./data/user.json', users)
      return redirect(url_for('login'))

  return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    users = read_file('./data/user.json')
    is_existing = False
    for user in users:
      if user['username'] == username and user['password'] == password:
        is_existing = True
        break
    if is_existing:
      return redirect(url_for('welcome', username=request.form['username']))
    else:
      error = 'Invalid Credentials. Please try again.'  
  return render_template('login.html', error=error)



@app.route('/welcome/<username>')
def welcome(username):
  return render_template('welcome.html', username=username)




def read_file(src_file):
  with open(src_file, 'r') as file:
    content = json.load(file)
    return content 

def write_to_file(des_file, data):
  with open(des_file, 'w') as outfile:
    json.dump(data, outfile) 