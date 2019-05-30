from flask import Flask, render_template
from db_services import write_to_js_file, count_msg_by_user, count_reactions, reaction_user_counter, avg_msg_counter_hour_day


app = Flask(__name__)


@app.route("/")
def index():
  data_file_name = './static/js/user_msg_counter_data.js'
  user_msg_counter = count_msg_by_user()
  write_to_js_file(data_file_name, user_msg_counter)
  
  reaction_counter_file = './static/js/reaction_counter_data.js'
  reaction_counter = count_reactions()
  write_to_js_file(reaction_counter_file, reaction_counter)

  reaction_user_counter_file = './static/js/reaction_user_counter_data.js'
  most_reaction_user_counter = reaction_user_counter()
  write_to_js_file(reaction_user_counter_file, most_reaction_user_counter)

  avg_msg_counter_hour_day_file = './static/js/avg_msg_counter_hour_day_data.js'
  [avg_msg_counter_hour_day_data, start_date, end_date] = avg_msg_counter_hour_day()
  write_to_js_file(avg_msg_counter_hour_day_file, avg_msg_counter_hour_day_data)
  return render_template("index.html",start_date=start_date, end_date=end_date)

@app.route("/blogs")
def list_blogs():
    return render_template("blogs.html")

@app.route("/archive")
def archive():
    return render_template("archive.html")

@app.route("/tags")
def tags():
    return render_template("tags.html")

@app.route("/about")
def about():
    return render_template("about.html")