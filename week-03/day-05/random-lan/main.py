from flask import Flask, render_template
import random

app = Flask(__name__)

greetings_list = ['Hey,', 'How’s it going?', 'How are you doing?', 'What’s new?', 'How’s everything ?', 'Good to see you', 'Long time no see', 'It’s been a while', 'It’s nice to meet you', 'How do you do?', 'How have you been?']
name_list = ['Claire', 'Ke', 'Sara', 'Levi', 'Steven', 'Yu', 'Payne', 'Angela', 'Haoxiang', 'Changdong', 'Yuan', 'Santi', 'Ted', 'Ray']

@app.route('/')
def index():
  greeting = random_item_from_list(greetings_list)
  name = random_item_from_list(name_list)
  return render_template('index.html', greeting=greeting, name=name)


def random_item_from_list(item_list):
  return item_list[random.randint(0, len(item_list))]