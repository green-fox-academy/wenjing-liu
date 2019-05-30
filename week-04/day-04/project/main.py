from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

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