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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Full_Name = request.form['Full_name']
        Email = request.form['Email']
        Password = request.form['Password']
        Confirm_password = request.form['Confirm_password']
        City = request.form['City']
        State = request.form['State']

        if Password == Confirm_password:
            pw_hash = bcrypt.generate_password_hash(Password).decode('utf-8')
            mongo.db.users.insert_one(
                {
                    "fullName": Full_Name,
                    "email": Email,
                    "password": pw_hash,
                    "city": City,
                    "state": State

                }
            )
            flash("Account created Successfully", "success")
            return redirect(url_for('login'))
        else:
            flash('Password and confirm password are not same', 'danger')
    return render_template("signup.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        Email = request.form["Email"]
        Password = request.form["Password"]
        found_user = mongo.db.users.find_one({"email": Email})
        if found_user:
            if bcrypt.check_password_hash(found_user['password'], request.form['Password']):
                session['fullName'] = found_user['fullName']
                session['email'] = found_user['email']
                flash("Successful Login", "success")
                return redirect(url_for("index"))
            else:
                flash("Login failed. Please try again!", "danger")
        else:
            flash("Sorry user not found", "danger")
    return render_template("login.html")


@app.route("/add_blog")
def add_blog():
    return render_template("add_blog.html")


if __name__ == "__main__":
    app.secret_key = "asdtc"
    app.run(debug=True)
