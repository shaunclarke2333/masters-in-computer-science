from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session
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

# rows, column_names = trip_service.get_view_all_trips()
# print(make_dataframe(rows, column_names))

# Creating the web app
app = Flask(__name__)

# Creating dummy secret key for login sessions
app.secret_key = "just-a-dummy-key"


# Creating homepage route
@app.route("/")
def home():
    return render_template("index.html")


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
            # validate the users credentials
            if username == "admin" and password == "secret":
                # Saving authenticated username in session to use throught the session
                session["username"] = username
                
                username = session.get("username")
                # Confimring login to user and starting session with flasj
                flash("Logged in successfully!")
                # Converting first letter in name to uppercase
                username = username.capitalize()
                # redirecting logged in user to their dashboard
                return redirect(url_for("dashboard", username=username))
            else:
                error = "Invalid username or password."

    # GET or failed POST: re-render form
    return render_template("login.html", error=error)


# Creating dashboard route
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        flash("Please log in first.")
        return redirect(url_for("login"))
    
    return render_template("dashboard.html")


# Creating add passenger route with variables needed to add passenger to DB
@app.route("/add-passenger", methods=["GET", "POST"])
def add_passenger():

    # Setting validation error place holder if anything form related fails
    error = None

    if request.method == "POST":
        """
        Stripping whitespace from input.
        using empty quotes to ensure app does not crash
        """  
        first_name: str = request.form.get("first_name", "").strip()
        last_name: str = request.form.get("last_name", "").strip()
        phone: str = request.fomr.get("phone", "").strip()

        if not first_name or not last_name or not phone:
            error = "First name, Last name and Phone are required"
        else:
            try:
                rows, column_names = passenger_service.add_passenger(first_name, last_name, phone)
                if rows is not None:
                    added_user_id: int = rows[0][0]
                    if isinstance(added_user_id, int):
                        # Confimring Passenger was added and starting session with flasj
                        flash("Passenger added successfully!")
                        #redirecting user back to their dashboard with their username to display
                        username = session.get("username")
                        return redirect(url_for("dashboard", username=username))
                    
                    raise ValueError(f"Passenger was not added")
                else:
                    raise ValueError(f"Passenger was not added")
                    
            except Exception as err:
                error = err
                return render_template("add_passenger.html", error=error)

    

 
# Creating add vessel route
@app.route("/add-vessel", methods=["GET", "POST"])
def add_vessel():
    
    # Setting validation error place holder if anything form related fails
    error = None

    # Logic to run if the users submits the form
    if request.method == "POST":
        """
        Stripping whitespace from input.
        using empty quotes to ensure app does not crash
        """  
        vessel_name: str = request.form.get("vessel_name", "").strip()
        cost_per_hr: int = request.form.get("cost_per_hr", "").strip()

        if not vessel_name or not cost_per_hr:
            error = "Vessel name and cost per hr are required"
        else:
            try:
                rows, column_names = vessel_service.add_vessel(vessel_name, cost_per_hr)
                if rows is not None:
                    added_vessel_id: int = rows[0][0]
                    if isinstance(added_vessel_id, int):
                        # Confimring vessel was added and starting session with flash
                        flash("Vessel added successfully!")
                        #redirecting user back to their dashboard with their username to display
                        username = session.get("username")
                        return redirect(url_for("dashboard", username=username))
                    
                    raise ValueError(f"Vessel was not added")
                else:
                    raise ValueError(f"Vessel was not added")
                    
            except Exception as err:
                error = err
                return render_template("add_vessel.html", error=error)

# # Creating add trip route
# @app.route("/add-trip", ["GET", "POST"])
# # Creating view all trips route
# def add_trip():

#     # Setting validation error place holder if anything form related fails
#     error = None

#     # Logic to run if the users submits the form
#     if request.method == "POST":
#         """
#         Stripping whitespace from input.
#         using empty quotes to ensure app does not crash
#         """  
#         vessel_name: str = request.form.get("vessel_name", "").strip()
#         first_name: str = request.form.get("first_name", "").strip()
#         last_name: str = request.form.get("last_name", "").strip()
#         date: str = request.form.get("date", "").strip()
#         time: str = request.form.get("time", "").strip()
#         trip_length: str = request.form.get("trip_length", "").strip()
#         total_passengers: str = request.form.get("total_passengers", "").strip()

#         if not vessel_name or not cost_per_hr:
#             error = "Vessel name and cost per hr are required"
#         else:
#             try:
#                 rows, column_names = vessel_service.add_vessel(vessel_name, cost_per_hr)
#                 if rows is not None:
#                     added_vessel_id: int = rows[0][0]
#                     if isinstance(added_vessel_id, int):
#                         # Confimring vessel was added and starting session with flash
#                         flash("Vessel added successfully!")
#                         #redirecting user back to their dashboard with their username to display
#                         username = session.get("username")
#                         return redirect(url_for("dashboard", username=username))
                    
#                     raise ValueError(f"Vessel was not added")
#                 else:
#                     raise ValueError(f"Vessel was not added")
                    
#             except Exception as err:
#                 error = err
#                 return render_template("add_vessel.html", error=error)


@app.route("/all-trips-view")
def all_trips_view():
    rows, column_names = trip_service.get_view_all_trips()
    return render_template("view_all_trips.html", rows=rows, column_names=column_names)


@app.route("/test/<name>")
def test(name):
    return render_template("test.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
