from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from typing import List, Tuple
import pandas as pd
import mysql.connector
import configparser
import dal
import bll


# This method formats output
def output_separator(input_text: str) -> str:
    """
    - This method formats text and outputs it with separators.
    - Returns a string.
    """
    print("\n" + "="*50)
    print(f" {input_text} ")
    print("="*50)


# This function handles converting the SQL output to a dataframe
def make_dataframe(rows: List, column_names: List) -> str:
    """
    - Converts query output to a dataframe.
    - returns a str.
    """
    # Using pandas to convert data to dataframe, also using to string method to remove index.
    df = pd.DataFrame(rows, columns=column_names)
    print(df.to_string(index=False, justify='center'))

# Creating config parser object to access database configurations.
config = configparser.ConfigParser()

# Reading config file
config.read("config.ini")

# Createing DB connection
connection = dal.ManageDbConnection(
    host=config['Database']['host'],
    user=config['Database']['user'],
    port=config['Database']['port'],
    database=config['Database']['database'],
    password=config['Database']['password']
)
# Connecting to DB
connection.connect_to_db()

# Passing connection to DatabaseActions
db_actions = dal.DatabaseActions(connection)

# Passing DAL to BLL services
vessel_service = bll.VesselService(dal.VesselsDal(db_actions))
passenger_service = bll.PassengerService(dal.PassengersDal(db_actions))
trip_service = bll.TripService(dal.TripsDal(db_actions))

# Creating the web app
app = Flask(__name__)


# Creating homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Creating view all trips route
@app.route("/all-trips-view")
def all_trips_view():
    rows, column_names = trip_service.get_view_all_trips()
    return render_template("index.html", rows=rows, column_names=column_names)

# Creating login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        # --- Basic server-side validation ---
        if not username or not password:
            error = "Username and password are required."
        else:
            # TODO: replace this with a real BLL call
            # e.g. user = user_service.authenticate(username, password)
            if username == "admin" and password == "secret":
                # flash("Logged in successfully!")
                return redirect(url_for("all_trips_view"))
            else:
                error = "Invalid username or password."

    # GET or failed POST: re-render form
    return render_template("login.html", error=error)



@app.route("/test/<name>")
def test(name):
    return render_template("test.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
