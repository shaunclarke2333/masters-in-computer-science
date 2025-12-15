"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 08: Final Oroject
"""

import mysql.connector
from typing import List, Tuple
from datetime import datetime



# This class manages the database connection
class ManageDbConnection:
    def __init__(self, host: str, user: str, port: int, database: str, password: str):
        self._host = host
        self._user = user
        self._port = port
        self._database = database
        self._password = password
        self._db_object = None
        self._cursor = None
        self._is_connected: bool = False
        self._has_cursor: bool = False

    # This method connects to the database
    def connect_to_db(self):
        """
        - This method conects to the specified DB.
        """

        try:
            # Logic to only connect to the DB if it is not connected.
            if not self._is_connected:
                # Establishing DB connection with params
                self._db_object = mysql.connector.connect(
                    host=self._host,
                    user=self._user,
                    port=self._port,
                    database=self._database,
                    password=self._password
                )

                # Creating Cursor
                self._cursor = self._db_object.cursor()
                # Setting cursor and connection status
                self._has_cursor = True
                self._is_connected = True

        except mysql.connector.Error:
            # Updating cursor and connection status
            self._has_cursor = False
            self._is_connected = False
            raise

    # This method gets the DB connection
    def get_connection(self) -> object:
        if not self._is_connected or self._db_object is None:
            raise mysql.connector.Error(
                f"Database is not connected. Connect DB first.")
        return self._db_object

    # This method gets the cursor
    def get_cursor(self) -> object:
        if not self._has_cursor or self._cursor is None:
            raise mysql.connector.Error(
                f"Cursor doesn't exist. Make sure DB is connected and cursor was created.")
        return self._cursor

    # This method gets cursor status
    def get_cursor_status(self):
        return self._has_cursor

    # This method gets connections status
    def get_connection_status(self):
        return self._is_connected

    # This method closes the cursor
    def close_cursor(self):
        """
        - This method closes the cursor.
        - returns nothing.
        """
        if self._cursor is not None:
            self._cursor.close()
            # Setting cursor object to None to cleanup cursor connection
            self._cursor = None
            # Updating cursor status
            self._has_cursor: bool = False

    # This method closes the db connection
    def close_db_connection(self):
        """
        - This method closes the DB connection.
        - returns nothing.
        """
        # if the DB object is present close it
        if self._db_object is not None:
            self._db_object.close()
            # Setting database object to None to cleanup closed connection
            self._db_object = None
            # Updating DB connection status
            self._is_connected: bool = False


# This class manages the database crud actions
class DatabaseActions:
    def __init__(self, connection: ManageDbConnection):
        if not connection.get_connection_status():
            raise mysql.connector.Error(
                "DatabaseActions requires an active connection")
        self._db: object = connection.get_connection()  # Getting the DB object
        self._cursor: object = connection.get_cursor()  # Creating cursor object

    # This method performs a select query
    def select_query(self, query: str, params: tuple | None = None) -> Tuple[list[tuple], List[str]]:
        """
        - This method runs select queries(Select, functions, views etc).
        - Returns raw data, rows and column names.
        """
        # Executing query
        self._cursor.execute(query, params)
        # Getting rows and column headers from output
        column_names: List = self._cursor.column_names
        rows: List = self._cursor.fetchall()

        return rows, column_names

    # This method handles procedure calls
    def procedure_calls(self, proc_name: str, params: Tuple | None = None) -> Tuple[list[tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        self._cursor.callproc(proc_name, params)

        # Lists for rows and columns data
        rows = []
        column_names = []

        # parsing output to get rows and columns headers
        for results in self._cursor.stored_results():
            column_names: List = results.column_names
            rows: List = results.fetchall()
        return rows, column_names

    def commit(self):
        self._db.commit()
        

# This class handles the database interactions for user charts in their dashboard.
class UserChartsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    
    # This method returns data from the workoutsummariees view
    def workout_saummarry_view(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for workout_saummarry_view
        
        :param self: Description
        :return: raw data, rows and column names
        :rtype: Tuple[list[tuple], List[str]]
        """
        
        # Getting all rows from the workoutsummaries view
        query_output = self._db_actions.select_query("SELECT * FROM workoutSummaries")
        return query_output
    
    # This method returns data from the dailyMoodTrends view
    def daily_mood_trends_view(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for daily_mood_trends_view
        
        :param self: Description
        :return: raw data, rows and column names
        :rtype: Tuple[list[tuple], List[str]]
        """
        
        # Getting all rows from the dailyMoodTrends view
        query_output = self._db_actions.select_query("SELECT * FROM dailyMoodTrends")
        return query_output
    
    # This method returns data from the caloriesPerDaySummaries view
    def calories_perday_saummary_view(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for calories_perday_saummary_view
        
        :param self: Description
        :return: raw data, rows and column names
        :rtype: Tuple[list[tuple], List[str]]
        """
        
        # Getting all rows from the caloriesPerDaySummaries view
        query_output = self._db_actions.select_query("SELECT * FROM caloriesPerDaySummaries")
        return query_output
    
    # This method returns data from the dailyWeightSummary view
    def daily_weight_summary_view(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for daily_weight_summary_view
        
        :param self: Description
        :return: raw data, rows and column names
        :rtype: Tuple[list[tuple], List[str]]
        """
        
        # Getting all rows from the dailyWeightSummary view
        query_output = self._db_actions.select_query("SELECT * FROM dailyWeightSummary")
        return query_output
    


# This class handles interaction with the exercise table
class ExerciseDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from exercise table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the exercises table
        query_output = self._db_actions.select_query("SELECT * FROM exercises")
        return query_output
    

# This class handles interaction with the food table
class FoodDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from food table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the exercises table
        query_output = self._db_actions.select_query("SELECT * FROM food")
        return query_output

    

# This class handles interaction with the vessels table
class MealItemsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from meal_items table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the meal_items table
        query_output = self._db_actions.select_query("SELECT * FROM meal_items")
        return query_output


    # This method adds items to meal items table
    def add_meal_item_proc(self, meal_id: int,  food_name: str, servings: int) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_meal_item_proc procedure
        
        :param self: Description
        :param meal_id: Description
        :type meal_id: int
        :param food_name: Description
        :type food_name: str
        :param servings: Description
        :type servings: int
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """

        proc_params = (meal_id, food_name, servings)
        # calling the addmealitems procedure
        rows, column_names = self._db_actions.procedure_calls(
            "addMealItem", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names


# This class handles interaction with the meals table
class MealsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from meals table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the meals table
        query_output = self._db_actions.select_query("SELECT * FROM meals")
        return query_output


    # This method adds a meal to the meals table
    def add_meal_proc(self, username: str, meal_date_time: str, meal_type: str, notes: str, meal_id_output=None) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_meal_proc
        
        :param self: Description
        :param username: Description
        :type username: str
        :param meal_date_time: Description
        :type meal_date_time: str
        :param meal_type: Description
        :type meal_type: str
        :param notes: Description
        :type notes: str
        :param meal_id_output: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        proc_params = (username, meal_date_time, meal_type, notes, meal_id_output)
        # calling the add meal procedure
        rows, column_names = self._db_actions.procedure_calls(
            "addMeal", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names
    

# This class handles interaction with the mood_entries table
class MoodEntriesDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from mood_entries table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the mood_entries table
        query_output = self._db_actions.select_query("SELECT * FROM mood_entries")
        return query_output

    # This method adds a mmod log to the logMood table
    def log_mood_proc(self, username: str, date_time: str, mood_score: int, energy_level: int, stress_level: int, note: str) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_vessel_proc
        
        :param self: Description
        :param username: Description
        :type username: str
        :param date_time: Description
        :type date_time: str
        :param mood_score: Description
        :type mood_score: int
        :param energy_level: Description
        :type energy_level: int
        :param stress_level: Description
        :type stress_level: int
        :param note: Description
        :type note: str
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        proc_params = (username, date_time, mood_score, energy_level, stress_level, note)
        # calling the add logMood procedure
        rows, column_names = self._db_actions.procedure_calls(
            "logMood", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names


# This class handles interaction with the users table
class UsersDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from users table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting logged in user details from the users table
        query_output = self._db_actions.select_query(f"SELECT * FROM users")
        return query_output
    
    # This method returns all rows for a specific user from users table
    def get_user_details(self, logged_in_user) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # Query params
        params = (logged_in_user,)
        # Query
        query = "SELECT first_name, last_name, email, username, date_of_birth, gender, height, weight FROM users WHERE username = %s"
        # getting logged in user details from the users table
        query_output = self._db_actions.select_query(query, params)
        return query_output

    # This method adds a user to the user's table
    def create_user_proc(self, first_name: str, last_name: str, email: str, password: str, username: str, dob: str, gender: str, height: int, weight: int) -> Tuple[List[Tuple], List[str]]:

        # Geting the current date and time
        now = datetime.now()

        # Formatting the datetime object into the desired string format that the created at column expects
        created_at_date = now.strftime("%Y-%m-%d %H:%M:%S")
        
        proc_params = (first_name, last_name, email, password, created_at_date, username, dob, gender, height, weight)
        # calling the createUser procedure
        rows, column_names = self._db_actions.procedure_calls(
            "createUser", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names

    # This method delete's a user account
    def delete_account_proc(self, username: str) -> Tuple[List[Tuple], List[str]]:
        
        proc_params = (username,)
        # calling the deleteAccount procedure
        rows, column_names = self._db_actions.procedure_calls(
            "deleteAccount", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names
    

    # This method allows a user to reset their password
    def reset_passwordr_proc(self, email: str, password: str, username: str) -> Tuple[List[Tuple], List[str]]:
        
        proc_params = (email, password, username)
        # calling the resetPassword procedure
        rows, column_names = self._db_actions.procedure_calls(
            "resetPassword", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names
    

# This class handles interaction with the weight_logs table
class WeightLogsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from weight_logs table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the weight_logs table
        query_output = self._db_actions.select_query("SELECT * FROM weight_logs")
        return query_output

    # This method adds the user's weight to the weight_logs table
    def log_user_weight_proc(self, username: str, weight: int, created_at_date: str) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for log_user_weight_proc
        
        :param self: Description
        :param username: Description
        :type username: str
        :param weight: Description
        :type weight: int
        :param created_at_date: Description
        :type created_at_date: str
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        proc_params = ( username, weight, created_at_date)
        # calling the logWeight procedure
        rows, column_names = self._db_actions.procedure_calls(
            "logWeight", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names
    

# This class handles interaction with the workout_sessions table
class WorkoutSessionsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from workout_sessions table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the workout_sessions table
        query_output = self._db_actions.select_query("SELECT * FROM workout_sessions")
        return query_output

    # This method adds the user's workouts to the workout_sessions table
    def log_user_workout_proc(self, username: str, exercise: str, date_time: str, duration_in_minutes: int, notes: str, sets: int, reps: int, weight: int) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for log_user_workout_proc
        
        :param self: Description
        :param username: Description
        :type username: str
        :param exercise: Description
        :type exercise: str
        :param date_time: Description
        :type date_time: str
        :param duration_in_minutes: Description
        :type duration_in_minutes: int
        :param notes: Description
        :type notes: str
        :param sets: Description
        :type sets: int
        :param reps: Description
        :type reps: int
        :param weight: Description
        :type weight: int
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        proc_params = (username, exercise, date_time, duration_in_minutes, notes, sets, reps, weight)
        # calling the logWorkout procedure
        rows, column_names = self._db_actions.procedure_calls(
            "logWorkout", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names







###################################
# This class handles interaction with the vessels table
class VesselsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from vessles table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """
        Docstring for get_all_rows
        
        :param self: Description
        :return: raw data, rows and column names.
        :rtype: Tuple[list[tuple], List[str]]
        """
        # getting all rows from the vessel table
        query_output = self._db_actions.select_query("SELECT * FROM vessels")
        return query_output

    # This method calls the get vesssel ID function
    def get_vessel_id(self, vessel_name: str) -> Tuple[List[Tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        func_params = (vessel_name,)
        # Calling the vessel ID function
        rows, column_names = self._db_actions.select_query(
            "SELECT getVesselID(%s)", func_params)
        return rows, column_names

    # This method adds a vessel to the vessels table
    def add_vessel_proc(self, vessel_name: str, cost_per_hr: int) -> Tuple[List[Tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        proc_params = (vessel_name, cost_per_hr)
        # calling the add vessel procedure
        rows, column_names = self._db_actions.procedure_calls(
            "addVessel", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names

    # This method calls the total revenue By vessel view
    def get_total_rev_view(self) -> Tuple[List[Tuple], List[str]]:
        """
        #
        - Returns raw data, rows and column names.
        """
        query = ("SELECT * FROM `total revenue By vessel`")
        # getting all rows from the vessel table
        query_output = self._db_actions.select_query(query)
        return query_output
    

# This class handles interaction with the passengers table
class PassengersDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from passengers table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        # getting all rows from the passenger table
        query_output = self._db_actions.select_query(
            "SELECT * FROM passengers")
        return query_output

    # This method calls the get passenger ID function
    def get_passenger_id(self, first_name: str, last_name: str) -> Tuple[List[Tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        func_params = (first_name, last_name,)
        # Calling the passenger ID function
        rows, column_names = self._db_actions.select_query(
            "SELECT getPassengerID(%s, %s)", func_params)
        return rows, column_names

    # This method adds a passenger to the passengers table
    def add_passenger_proc(self, first_name: str, last_name: str, phone: str) -> Tuple[List[Tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        proc_params = (first_name, last_name, phone)
        # calling the add passenger procedure
        rows, column_names = self._db_actions.procedure_calls(
            "addPassenger", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names


# This class handles interaction with the trips table
class TripsDal:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from trips table
    def get_all_rows(self) -> Tuple[list[tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        # getting all rows from the trip table
        query_output = self._db_actions.select_query("SELECT * FROM trips")
        return query_output

    # This method adds a trip to the trips table
    def add_trip_proc(self, vessel_name: str, first_name: str, last_name: str, date: str, time: str,
                      trip_length: int, total_passengers: int) -> Tuple[List[Tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        proc_params = (vessel_name, first_name, last_name, date,
                       time, trip_length, total_passengers)
        # calling the add trip procedure
        rows, column_names = self._db_actions.procedure_calls(
            "addTrip", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names

    # This method gets all the rows from the all trips view
    def get_all_trips_view(self) -> Tuple[List[Tuple], List[str]]:
        """

        - Returns raw data, rows and column names.
        """
        query = ("SELECT * FROM `all trips`")
        # getting all rows from the all trips view
        query_output = self._db_actions.select_query(query)
        return query_output
    
     # This method checks if a vessel is already booked for the given date and time
    def check_vessel_conflict(self, vessel_name: str, date: str, time: str) -> int:
        """
        - Returns the number of trips found for the given vessel, date, and time.
        - Uses the GETVESSELID function so we do not need to know the underlying table structure.
        """
        sql = """
            SELECT COUNT(*) AS total
            FROM trips
            WHERE Vessel_ID = GETVESSELID(%s)
              AND Date = %s
              AND Departure_Time = %s
        """
        rows, column_names = self._db_actions.select_query(sql, (vessel_name, date, time))
        # rows[0][0] will be the count
        return rows[0][0]

    # This method checks if a passenger is already booked for the given date and time
    def check_passenger_conflict(self, first_name: str, last_name: str,
                                 date: str, time: str) -> int:
        """
        - Returns the number of trips found for the given passenger, date, and time.
        - Uses the GETPASSENGERID function so we do not need to know the underlying table structure.
        """
        sql = """
            SELECT COUNT(*) AS total
            FROM trips
            WHERE Passenger_ID = GETPASSENGERID(%s, %s)
              AND Date = %s
              AND Departure_Time = %s
        """
        rows, column_names = self._db_actions.select_query(
            sql, (first_name, last_name, date, time)
        )
        return rows[0][0]
