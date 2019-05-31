from flask import Flask, render_template
from db_services import write_to_js_file, count_msg_by_user, count_reactions, reaction_user_counter, avg_msg_counter_hour_day, thank_counter_msg_counter,  mentioned_users_for_thanks, msg_user_counter


app = Flask(__name__)


@app.route("/")
def index():
  avg_msg_counter_hour_day_file = './static/js/avg_msg_counter_hour_day_data.js'
  [avg_msg_counter_hour_day_data, start_date, end_date] = avg_msg_counter_hour_day()
  write_to_js_file(avg_msg_counter_hour_day_file, avg_msg_counter_hour_day_data)
  thank_to_all_ratio_file = './static/js/thank_to_all_ratio_data.js'
  thank_to_all_data = thank_counter_msg_counter()
  write_to_js_file(thank_to_all_ratio_file, thank_to_all_data)
  data_info = msg_user_counter()
  return render_template("index.html",start_date=start_date, end_date=end_date, data_info=data_info)

@app.route("/users")
def list_blogs():
  reaction_user_counter_file = './static/js/reaction_user_counter_data.js'
  most_reaction_user_counter = reaction_user_counter()
  write_to_js_file(reaction_user_counter_file, most_reaction_user_counter)

  data_file_name = './static/js/user_msg_counter_data.js'
  user_msg_counter = count_msg_by_user()
  write_to_js_file(data_file_name, user_msg_counter)
  return render_template("users.html")

@app.route("/mentions")
def mentions():
  mentioned_users_for_thanks_file = './static/js/mentioned_users_for_thanks_data.js'
  mentioned_users_for_thanks_data = mentioned_users_for_thanks()
  write_to_js_file(mentioned_users_for_thanks_file, mentioned_users_for_thanks_data)
  return render_template("mentions.html")

@app.route("/reactions")
def reaction():
  reaction_counter_file = './static/js/reaction_counter_data.js'
  reaction_counter = count_reactions()
  write_to_js_file(reaction_counter_file, reaction_counter)
  return render_template("reactions.html")