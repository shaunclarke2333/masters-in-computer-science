"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 08: Final Oroject
"""

from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from functools import wraps
from datetime import datetime
from typing import List, Tuple
# import time
import pandas as pd
import mysql.connector
import configparser
import dal
import bll



def get_dal_actions(
    connection,
    DatabaseActions=dal.DatabaseActions,
    UserChartsDal=dal.UserChartsDal,
    ExerciseDal=dal.ExerciseDal,
    FoodDal=dal.FoodDal,
    MealsDal=dal.MealsDal,
    MealItemsDal=dal.MealItemsDal,
    UsersDal=dal.UsersDal,
    WeightLogsDal=dal.WeightLogsDal,
    WorkoutSessionsDal=dal.WorkoutSessionsDal,
):
    
    # Creating shared DB actions object
    db_actions = DatabaseActions(connection)

    # Instantiate DALs
    return {
        "user_charts": UserChartsDal(db_actions),
        "exercise": ExerciseDal(db_actions),
        "food": FoodDal(db_actions),
        "meal": MealsDal(db_actions),
        "meal_items": MealItemsDal(db_actions),
        "users": UsersDal(db_actions),
        "weight_logs": WeightLogsDal(db_actions),
        "workout_sessions": WorkoutSessionsDal(db_actions),
    }



app = Flask(__name__)

# Dummy secret key so we can use session
app.secret_key = "some-dummy-key"

# Getting the database connection
def get_db_connection(db_connection_manager_dal = dal.ManageDbConnection):

    # Validating that the DB is connected
    if not session.get("db_connected"):
        raise mysql.connector.Error("DB not connected")
    
    connection = db_connection_manager_dal(
        host="localhost",
        port = 3306,
        user=session.get("db_user"),
        password=session.get("db_pass"),
        database="mbd"
    )

    # connecting database
    connection.connect_to_db()
    
    # Proceeding to return a DB connection if DB is connected
    return connection


# Creating a decorator to use with routes that require a database connection.
# User gets notified if the database is not connected.
def deb_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not session.get("db_connected"):
            flash("Database is not connected. Click the DB button in the navbar to connect.", "warning")
            return redirect(url_for("home"))
        return view_func(*args, **kwargs)
    return wrapper



# Creating homepage route
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Database connection route
@app.route("/db/connect", methods=["POST"])
def connect_db():
    # Creating json object to fetch entered db creds
    db_info = request.get_json(silent=True) or {}
    db_user = (db_info.get("db_user") or "").strip()
    db_pass = db_info.get("db_pass") or ""

    # error message to handle if db creds were not entered
    if not db_user or not db_pass:
        return jsonify(ok=False, message="Username and password required."), 400

    try:
        # Createing DB connection
        connection = dal.ManageDbConnection(
            host="localhost",
            port = 3306,
            user=db_user,
            password=db_pass,
            database="mbd"
        )
        
        # Connecting to DB
        connection.connect_to_db()

        # checking connection status
        connection_status = connection.get_connection_status()
        if not connection_status:
            raise mysql.connector.Error(f"Database connection failed")
        

        # If connection status check passed, update db_conected in session to true for DB sessions tate and add the db user and pass to session
        # This allows the connection to persist for the session
        # This is not best practice to store password in session, i am only doing it for this project and due to time constraints.
        session["db_connected"] = True
        session["db_user"] = db_user
        session["db_pass"] = db_pass

        # Returning JSON object 
        return jsonify(ok=True)
    
    except Exception:
        # Removing everything from session to cleanup and reset session state
        session.pop("db_connected", None)
        session.pop("db_user", None)
        session.pop("db_pass", None)
        # Returning a json object with error message
        return jsonify(ok=False, message="Invalid DB credentials."), 401




#"signin" endpoint for "/signin"
@app.route("/signin", methods=["GET", "POST"])
# Alerts the user if they try to do anything befor connecting the DB.
@deb_required
def signin():
    # setting error variable
    error = None
    if session.get("user_id"):
        # redirecting user to dashboard
        return render_template("dashboard.html")
    
    # Getting user input from login form
    if request.method == "POST":
        """
        Stripping whitespace from input.
        using empty quotes to ensure app does not crash
        """
        username: str = request.form.get("username", "").strip()
        password: str = request.form.get("password", "").strip()

        # Doing server side validation to speed things up.
        if not username or not password:
            error: str = "Username and password are required."
        else:
            # Checking database to validate the users credentials

            # Getting DB connection
            connection = get_db_connection()
            # Creating database actions
            dal_actions = get_dal_actions(connection)
            #  validating user login

            users = bll.UserService(dal_actions.get("users"))
            rows, column_names = users.get_user_account(username, password)
            if rows[0][0] == 0:
                # Confimring login to user and starting session with flasj
                flash("Logged in successfully!", "success")
                # Saving authenticated username in session to use throught the session
                session["username"] = username

                # redirecting user to dashboard
                return redirect(url_for("dashboard"))

            if rows[0][0] == -1:
                # notifying user of failure
                flash("Invalid username or password.", "warning")
            if rows[0][0] == -2:
                flash("Invalid username or password.", "warning")

    # GET or failed POST: re-render form
    return render_template("signin.html")



#Some templates use url_for('index')
@app.route("/index", methods=["GET"])
def index():
    return redirect(url_for("home"))



@app.route("/contact", methods=["GET"])
def contact():
    return "Support (TODO)"


@app.route("/dashboard", methods=["GET"])
# Alerts the user if they try to do anything befor connecting the DB.
@deb_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    return "Forgot Password (TODO)"

@app.route("/delete-account")
def delete_account():
    return "delete account (TODO)"


@app.route("/signup", methods=["GET", "POST"])
# Alerts the user if they try to do anything befor connecting the DB.
@deb_required
def signup():
    return render_template("signup.html")


@app.route("/logout", methods=["GET"])
def logout():
    # Closing session which will logout the user
    session.clear()   
    flash("You have been logged out.", "success")
    return redirect(url_for("signin"))


@app.route("/account", methods=["GET"])
# Alerts the user if they try to do anything befor connecting the DB.
@deb_required
def account_settings():
    return render_template("account_settings.html")


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
    return render_template("workout_history.html")


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
    return render_template("weight_log.html")


@app.route("/weight/history", methods=["GET"])
def weight_history():
    return render_template("weight_history.html")


if __name__ == "__main__":
    app.run(debug=True)
