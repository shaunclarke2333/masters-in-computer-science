"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 08: Final Oroject
"""

from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session, current_app
from datetime import datetime
from typing import List, Tuple
# import time
import pandas as pd
import mysql.connector
import configparser
import dal
import bll




app = Flask(__name__)

pp = Flask(__name__)
app.secret_key = "some-dummy-key"  # needed because your templates reference session


#Make `current_app` available inside Jinja templates
@app.context_processor
def inject_current_app():
    return {"current_app": current_app}


#"home" endpoint for "/"
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("signin.html")


#"signin" endpoint for "/signin"
@app.route("/signin", methods=["GET", "POST"])
def signin():
    return render_template("signin.html")


#Some templates use url_for('index')
@app.route("/index", methods=["GET"])
def index():
    return redirect(url_for("home"))


#STUB ROUTES so url_for(...) in your theme never crashes
@app.route("/contact", methods=["GET"])
def contact():
    return "Support (TODO)"


@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    return "Forgot Password (TODO)"

@app.route("/delete-account")
def delete_account():
    return "delete account (TODO)"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return "Sign Up (TODO)"


@app.route("/logout", methods=["GET"])
def logout():
    return redirect(url_for("signin"))


@app.route("/account", methods=["GET"])
def account_settings():
    return render_template("account_settings.html")


# Optional stubs (only needed if your templates call these)
@app.route("/mood/log", methods=["GET", "POST"])
def mood_log():
    return render_template("mood_log.html")


@app.route("/mood/history", methods=["GET"])
def mood_history():
    return render_template("mood_history.html")


@app.route("/workout/log", methods=["GET", "POST"])
def workout_log():
    return render_template("workout_log.html")


@app.route("/workout/history", methods=["GET"])
def workout_history():
    return render_template("workout-log.htmk")


@app.route("/exercises", methods=["GET"])
def exercises():
    return "Exercise Library (TODO)"


@app.route("/food", methods=["GET"])
def food_library():
    return "Food Library (TODO)"


@app.route("/meals/create", methods=["GET", "POST"])
def meal_create():
    return render_template("meal_create.html")


@app.route("/meals/today", methods=["GET"])
def meals_today():
    return "Today's Meals (TODO)"


@app.route("/nutrition/summary", methods=["GET"])
def nutrition_summary():
    return "Nutrition Summary (TODO)"


@app.route("/weight/log", methods=["GET", "POST"])
def weight_log():
    return "Log Weight (TODO)"


@app.route("/weight/history", methods=["GET"])
def weight_history():
    return "Weight History (TODO)"


if __name__ == "__main__":
    app.run(debug=True)
