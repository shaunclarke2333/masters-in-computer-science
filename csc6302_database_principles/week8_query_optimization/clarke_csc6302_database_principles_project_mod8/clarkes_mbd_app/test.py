from flask import Flask
from flask import render_template, request, redirect, url_for, flash, session
from typing import List, Tuple
# import time
import pandas as pd
import mysql.connector
import configparser
import dal
import bll

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
db_actions: dal.DatabaseActions = dal.DatabaseActions(connection)

user_charts = dal.UserChartsDal(db_actions)
exercise = dal.ExerciseDal(db_actions)
food = dal.FoodDal(db_actions)
meal = dal.MealsDal(db_actions)
meal_items = dal.MealItemsDal(db_actions)
users = dal.UsersDal(db_actions)
weight_logs = dal.WeightLogsDal(db_actions)
workout_sessions = dal.WorkoutSessionsDal(db_actions)


# # Testing user charts views
# rows, column_names = user_charts.calories_perday_saummary_view()
# make_dataframe(rows, column_names)
# rows, column_names = user_charts.daily_mood_trends_view()
# make_dataframe(rows, column_names)
# rows, column_names = user_charts.daily_weight_summary_view()
# make_dataframe(rows, column_names)
# rows, column_names = user_charts.workout_saummarry_view()
# make_dataframe(rows, column_names)

# # testing exercise table actions
# rows, column_names = exercise.get_all_rows()
# make_dataframe(rows, column_names)

# # testing food table actions
# rows, column_names = food.get_all_rows()
# make_dataframe(rows, column_names)

# # testing meal table actions
# rows, column_names = meal.add_meal_proc('ShaunC', '2025-10-15 13:00:00', 'lunch', 'Tofu scramble and spinach')
# meal_id = rows[0][0]
# print()
# print(type(rows[0][0]))
# make_dataframe(rows, column_names)

# rows, column_names = meal.get_all_rows()
# make_dataframe(rows, column_names)

# # Testing meal_items table actions
# rows, column_names = meal_items.add_meal_item_proc(meal_id, 'Firm Tofu', 4)
# make_dataframe(rows, column_names)

# rows, column_names = meal_items.get_all_rows()
# make_dataframe(rows, column_names)


# # Testing users table actions
# rows, column_names = users.get_all_rows()
# make_dataframe(rows, column_names)

# rows, column_names = users.create_user_proc('Michael', 'Jordan', 'michael@example.com', 'hash_michael_123', 'MichaelJ', '1983-04-12',	'male',	185.42,	107.50)
# make_dataframe(rows, column_names)

# rows, column_names = users.get_all_rows()
# make_dataframe(rows, column_names)

# rows, column_names = users.reset_passwordr_proc('hash_michael_9', 'MichaelJ', 'michael@example.com')
# make_dataframe(rows, column_names)

# rows, column_names = users.get_all_rows()
# make_dataframe(rows, column_names)

# rows, column_names = users.delete_account_proc('MichaelJ')
# make_dataframe(rows, column_names)

# rows, column_names = users.get_all_rows()
# make_dataframe(rows, column_names)

# rows, column_names = users.get_user_details('ShaunC')
# make_dataframe(rows, column_names)


# # Testing weight log table actions
# rows, column_names = weight_logs.log_user_weight_proc('ShaunC', 107.20, '2025-10-11 07:00:00')
# make_dataframe(rows, column_names)

# rows, column_names = weight_logs.get_all_rows()
# make_dataframe(rows, column_names)

# # Testing weight log table actions
# rows, column_names = workout_sessions.log_user_workout_proc('ShaunC','Back Squat', '2025-10-10 05:45:00', 90, 'Back squat, focused on form', 4, 5,  80.00)
# make_dataframe(rows, column_names)

# rows, column_names = workout_sessions.get_all_rows()
# make_dataframe(rows, column_names)
