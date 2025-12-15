"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 08: Final Oroject
"""

from typing import List, Tuple, Optional
import dal


# This class manages UserCHartsDal interactions
class UserChartsService:
    def __init__(self, user_charts_table_actions: dal.UserChartsDal):
        self.user_charts_table_actions = user_charts_table_actions

    # This method gets the workout_saummarry from the workout_saummarry view
    def get_workout_saummarry(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_workout_saummarry

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from the workout_saummarry view
        rows, column_names = self.user_charts_table_actions.workout_saummarry_view()
        return rows, column_names

    # This method gets the daily_mood_trends from the daily_mood_trends view
    def get_daily_mood_trends(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_daily_mood_trends

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from the daily_mood_trends view
        rows, column_names = self.user_charts_table_actions.daily_mood_trends_view()
        return rows, column_names

    # This method gets the calories_perday_saummary from the calories_perday_saummary view
    def get_calories_perday_saummary(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_calories_perday_saummary

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from the calories_perday_saummaryview
        rows, column_names = self.user_charts_table_actions.calories_perday_saummary_view()
        return rows, column_names

    # This method gets the daily_weight_summary from the daily_weight_summary view
    def get_workout_saummarry(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_workout_saummarry

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from the daily_weight_summary view
        rows, column_names = self.user_charts_table_actions.daily_weight_summary_view()
        return rows, column_names


# This class manages ExerciseDal interactions
class ExerciseService:
    def __init__(self, exercise_table_actions: dal.ExerciseDal):
        self.exercise_table_actions = exercise_table_actions

    # This method gets all the exercises from the exercise db table
    def get_all_exercises(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_all_exercises

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from exercise table
        rows, column_names = self.exercise_table_actions.get_all_rows()
        return rows, column_names


# This class manages FoodDal interactions
class FoodService:
    def __init__(self, food_table_actions: dal.FoodDal):
        self.food_table_actions = food_table_actions

    # This method gets all the food from the food db table
    def get_all_foods(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_all_foods

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from food table
        rows, column_names = self.food_table_actions.get_all_rows()
        return rows, column_names


# This class manages MealItemsDal interactions
class MealItemsService:
    def __init__(self, meal_items_table_actions: dal.MealItemsDal):
        self.meal_items_table_actions = meal_items_table_actions

    # This method gets all meal_items from the meal_items db table
    def get_all_meal_items(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_all_meal_items

        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from meal_items table
        rows, column_names = self.meal_items_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a meal item to the meal_items table
    def add_meal_item(self, meal_id: int,  food_name: str, servings: int) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_meal_item

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

        # validating inputs
        if not isinstance(servings, int):
            raise ValueError(
                f"Servings must be a number")

        # adding vessel to vessel table
        rows, column_names = self.meal_items_table_actions.add_meal_item_proc(
            meal_id, food_name, servings)
        return rows, column_names


# This class manages MealItemsDal interactions
class MealsService:
    def __init__(self, meals_table_actions: dal.MealsDal):
        self.meals_table_actions = meals_table_actions

    # This method gets all meals from the meals db table
    def get_all_meal(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_all_meal
        
        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from meal_items table
        rows, column_names = self.meals_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a meal item to the meal_items table
    def add_meal(
            self, username: str, meal_date_time: str, meal_type: str,
            notes: str, meal_id_output: Optional[int] = None) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_meal
        
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
        :type meal_id_output: Optional[int]
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Validating inputs
        # if not vessel_name or not vessel_name.strip():
        #     raise ValueError(f"Vessel name cannot be empty")

        # Adding meal to table
        rows, column_names = self.meals_table_actions.add_meal_proc(
            username, meal_date_time, meal_type, notes, meal_id_output)
        # Getting meal ID row value from list of tuple
        meal_id = rows[0][0]

        # If we found a Meal ID
        if meal_id != -1:
            return rows, column_names

        # If no Meal ID found -1 will be the row value
        return rows, column_names


# This class manages MoodEntriesDal interactions
class MoodEntriesService:
    def __init__(self, mood_entries_table_actions: dal.MoodEntriesDal):
        self.mood_entries_table_actions = mood_entries_table_actions

    # This method gets all rows from the mood_entries db table
    def get_all_mood_entries(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from mood_entries table
        rows, column_names = self.mood_entries_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a mood entry to the mood_entries table
    def add_mood_entries(
            self, username: str, date_time: str, mood_score: int, energy_level: int,
            stress_level: int, note: Optional[int] = None) -> Tuple[List[Tuple], List[str]]:
       
        # validating inputs
        if not isinstance(mood_score, int) or mood_score > 10 or mood_score < 1:
            raise ValueError(
                f"Mood score must be a number from 1 - 10")
        if not isinstance(energy_level, int) or energy_level > 10 or energy_level < 1:
            raise ValueError(
                f"Energy level must be a number from 1 - 10")
        if not isinstance(stress_level, int) or stress_level > 10 or stress_level < 1:
            raise ValueError(
                f"Stress level must be a number from 1 - 10")

        # calling log mood procedure to add a mood to mood entries table
        rows, column_names = self.mood_entries_table_actions.log_mood_proc(
            username, date_time, mood_score, energy_level, stress_level, note)
        return rows, column_names
    

# This class manages UserDal interactions
class UserService:
    def __init__(self, users_table_actions: dal.UsersDal):
        self.users_table_actions = users_table_actions

    # This method gets all rows from the users db table
    def get_all_users(self) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_all_users
        
        :param self: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting all rows from users table
        rows, column_names = self.users_table_actions.get_all_rows()
        return rows, column_names
    
    # This method gets a specific user's details from the users db table
    def get_a_user_details(self, logged_in_user) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for get_a_user_details
        
        :param self: Description
        :param logged_in_user: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting specific user details from users table
        rows, column_names = self.users_table_actions.get_user_details(logged_in_user)
        return rows, column_names

    # This method adds a user to the users table
    def add_user(
            self, first_name: str, last_name: str, email: str, password: str,
            username: str, dob: str, gender: str, height: int, weight: int) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_user
        
        :param self: Description
        :param first_name: Description
        :type first_name: str
        :param last_name: Description
        :type last_name: str
        :param email: Description
        :type email: str
        :param password: Description
        :type password: str
        :param username: Description
        :type username: str
        :param dob: Description
        :type dob: str
        :param gender: Description
        :type gender: str
        :param height: Description
        :type height: int
        :param weight: Description
        :type weight: int
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        
        # Removing any leading or trailing white space
        parameters_to_strip = [first_name, last_name, email, password, username]
        stripped_parameters = [p.strip() for p in parameters_to_strip]

        first_name = stripped_parameters[0]
        last_name = stripped_parameters[1]
        email = stripped_parameters[2]
        password = stripped_parameters[3]
        username = stripped_parameters[4]
        
        # validating inputs
        if not isinstance(height, int) or height > 10 or height < 1:
            raise ValueError(
                f"Height must be a number from 1 - 10")
        if not isinstance(weight, int) or weight > 10 or weight < 1:
            raise ValueError(
                f"Weight must be a number from 1 - 10")
        
        # calling the create user procedure procedure to add a procedure to the users table
        rows, column_names = self.users_table_actions.create_user_proc(
            first_name, first_name, last_name, email, password, username, dob, gender, height, weight)
        return rows, column_names
    
    
    # This method updates the user's password in the user's table 
    def add_user(self, email: str, password: str, username: str) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for add_user
        
        :param self: Description
        :param email: Description
        :type email: str
        :param password: Description
        :type password: str
        :param username: Description
        :type username: str
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """

        # Removing any leading or trailing white space
        parameters_to_strip = [email, password, username]
        stripped_parameters = [p.strip() for p in parameters_to_strip]

        email = stripped_parameters[0]
        password = stripped_parameters[1]
        username = stripped_parameters[2]
        

        # validating inputs
        if email is None:
            raise ValueError(
                f"Email cannot be empty")
        if password is None:
            raise ValueError(
                f"Password cannot be empty")
        if username is None:
            raise ValueError(
                f"Username cannot be empty")
       
        # calling the create user procedure procedure to add a procedure to the users table
        rows, column_names = self.users_table_actions.reset_passwordr_proc(email, password, username)
        return rows, column_names
    
    # This method delete's a user from the users db table, which deletes the user's account
    def delete_user_account(self, logged_in_user) -> Tuple[List[Tuple], List[str]]:
        """
        Docstring for delete_user_account
        
        :param self: Description
        :param logged_in_user: Description
        :return: Description
        :rtype: Tuple[List[Tuple], List[str]]
        """
        # Getting specific user details from users table
        rows, column_names = self.users_table_actions.delete_account_proc(logged_in_user)
        return rows, column_names
    


# This class manages WeightLogsDal interactions
class WeightLogService:
    def __init__(self, weight_logs_table_actions: dal.WeightLogsDal):
        self.weight_logs_table_actions = weight_logs_table_actions

    # This method gets all rows from the weight_logs db table
    def get_all_weight_logs(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from weight_logs table
        rows, column_names = self.weight_logs_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a user's weight to the weight_logs table
    def log_user_weight(self, username: str, weight: int) -> Tuple[List[Tuple], List[str]]:
       
        # validating inputs
        if username is None:
            raise ValueError(
                f"Username cannot be empty")
        
        if not isinstance(weight, int) or weight > 10 or weight < 1:
            raise ValueError(
                f"Weight must be a number from 1 - 10")

        # calling log user weight procedure to add a users's weight to the weight table
        rows, column_names = self.weight_logs_table_actions.log_user_weight_proc(username, weight)
        return rows, column_names


# This class manages WorkoutSessionsDal interactions
class WorkoutSessionService:
    def __init__(self, workout_sessions_table_actions: dal.WorkoutSessionsDal):
        self.workout_sessions_table_actions = workout_sessions_table_actions

    # This method gets all rows from the workout_sessions db table
    def get_all_workout_sessions(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from workout_sessions table
        rows, column_names = self.workout_sessions_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a workout entry to the workout_sessions table
    def add_workout_session(
            self, username: str, exercise: str, date_time: str,
            duration_in_minutes: int, sets: int, reps: int, weight: int, notes: Optional[int]=None) -> Tuple[List[Tuple], List[str]]:
       
        # validating inputs
        if not isinstance(duration_in_minutes, int) :
            raise ValueError(
                f"Workout length must be a number")
        if not isinstance(sets, int):
            raise ValueError(
                f"Sets must be a number")
        if not isinstance(reps, int) :
            raise ValueError(
                f"Reps must be a number")
        if not isinstance(weight, int) :
            raise ValueError(
                f"Weight must be a number")

        # calling log user workout procedure to add a workout to workout_sessions table
        rows, column_names = self.workout_sessions_table_actions.log_user_workout_proc(
            username, exercise, date_time, duration_in_minutes, notes, sets, reps, weight)
        return rows, column_names

######################################

# This class manages the interaction between the view and Dal
class MRCAppService:
    """
    This class acts as an entry point for the front end calls.
    it also acts as and interface to the data access layer for DB calls.
    """

    def __init__(self, vessel_service: VesselService, trip_service: TripService, passenger_service: PassengerService):
        self.vessel_service = vessel_service
        self.trip_service = trip_service
        self.passenger_service = passenger_service

    # Fetching total revenue by vessel to display on the frontend

    def view_total_rev_by_vessel(self) -> Tuple[List[Tuple], List[str]]:
        # getting all rows from total rev view
        rows, column_names = self.vessel_service.get_total_rev_view()
        return rows, column_names

    # Fetching the vessel ID with match to display on the frontend
    def view_vessel_id_match(self, vessel_name_match) -> Tuple[List[Tuple], List[str]]:
        # Getting vessel id with match
        rows, column_names = self.vessel_service.get_vessel_id(
            vessel_name_match)
        return rows, column_names

    # Fetching the vessel ID with NO match to display on the frontend
    def view_vessel_id_no_match(self, vessel_name_no_match: str) -> Tuple[List[Tuple], List[str]]:
        # Getting vessel id NO match
        rows, column_names = self.vessel_service.get_vessel_id(
            vessel_name_no_match)
        return rows, column_names

    # Adds a passenger to the passsenger table
    def add_passenger(self, first_name: str, last_name: str, phone: str) -> Tuple[List[Tuple], List[str]]:
        rows, column_names = self.passenger_service.add_passenger(
            first_name, last_name, phone)
        return rows, column_names

    # adds a vessel to vessel table
    def add_vessel(self, vessel_name: str, cost_per_hr: int) -> Tuple[List[Tuple], List[str]]:
        rows, column_names = self.vessel_service.add_vessel(
            vessel_name, cost_per_hr)
        return rows, column_names

    # adding trip details with new passenger and new vessel to trips table
    def add_new_trip_details(self, vessel_name: str, first_name: str, last_name: str, date: str, time: str,
                             trip_length: int, total_passengers: int) -> Tuple[List[Tuple], List[str]]:
        """
        """
        # Adding new trip
        rows, column_names = self.trip_service.add_trip(
            vessel_name, first_name, last_name, date, time, trip_length, total_passengers)
        return rows, column_names

    # Fetiching all rows from the all trips view
    def view_get_all_trips(self) -> Tuple[List[Tuple], List[str]]:

        # getting all rows from All Trips view
        rows, column_names = self.trip_service.get_view_all_trips()
        return rows, column_names
