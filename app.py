from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
import random
import datetime
from uuid import uuid4
from flask import request
import requests

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/traveloggers"

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route("/")
def helo():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/add_blog")
def add_blog():
    return render_template("add_blog.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/single_blog")
def single_blog():
    return render_template("single_blog.html")

if __name__ == "__main__":
    app.secret_key = "asdtc"
    app.run(debug=True)