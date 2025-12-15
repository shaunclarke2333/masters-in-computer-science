"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 08: Final Oroject
"""

from typing import List, Tuple
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
        # Getting all rows from exercise table
        rows, column_names = self.exercise_table_actions.get_all_rows()
        return rows, column_names


# This class manages FoodDal interactions
class FoodService:
    def __init__(self, food_table_actions: dal.FoodDal):
        self.food_table_actions = food_table_actions

    # This method gets all the food from the food db table
    def get_all_foods(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from food table
        rows, column_names = self.food_table_actions.get_all_rows()
        return rows, column_names
    

# This class manages MealItemsDal interactions
class MealItemsService:
    def __init__(self, meal_items_table_actions: dal.MealItemsDal):
        self.meal_items_table_actions = meal_items_table_actions

    # This method gets all meal_items from the meal_items db table
    def get_all_meal_items(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from meal_items table
        rows, column_names = self.meal_items_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a meal item to the meal_items table
    def add_meal_item(self, meal_id: int,  food_name: str, servings: int) -> Tuple[List[Tuple], List[str]]:
        
        # validating inputs
        if not isinstance(servings, int):
            raise ValueError(
                f"Servings must be a number")
        
        # adding vessel to vessel table
        rows, column_names = self.meal_items_table_actions.add_meal_item_proc(meal_id, food_name, servings)
        return rows, column_names


# This class manages MealItemsDal interactions
class MealsService:
    def __init__(self, meals_table_actions: dal.MealsDal):
        self.meals_table_actions = meals_table_actions

    # This method gets all meals from the meals db table
    def get_all_meal(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from meal_items table
        rows, column_names = self.meals_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a meal item to the meal_items table
    def add_meal(self, username: str, meal_date_time: str, meal_type: str, notes: str, meal_id_output=None) -> Tuple[List[Tuple], List[str]]:
        
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







######################################
# This class manages VesselDal interactions
class VesselService:
    def __init__(self, vessels_table_actions: dal.VesselsDal):
        self.vessels_table_actions = vessels_table_actions

    # This method gets all vessels from the vessel db table
    def get_all_vessels(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from vessel table
        rows, column_names = self.vessels_table_actions.get_all_rows()
        return rows, column_names

    # This method gets the vessel id from the vessel db table
    def get_vessel_id(self, vessel_name: str) -> Tuple[List[Tuple], List[str]]:
        # Removing any leading or trailing white space
        vessel_name = vessel_name.strip()
        # Validating inputs
        if not vessel_name or not vessel_name.strip():
            raise ValueError(f"Vessel name cannot be empty")

        # Getting row id from vessel table
        rows, column_names = self.vessels_table_actions.get_vessel_id(
            vessel_name)
        # Getting row value from list of tuple
        vessel_id = rows[0][0]

        # If we found a vessel ID
        if vessel_id != -1:
            return rows, column_names

        # If no vessel ID found -1 will be the row value
        return rows, column_names

    # This method adds a vessel to the vessel table
    def add_vessel(self, vessel_name: str, cost_per_hr: int) -> Tuple[List[Tuple], List[str]]:
        # Removing any leading or trailing white space
        vessel_name = vessel_name.strip()
        # validating inputs
        if not isinstance(cost_per_hr, int):
            raise ValueError(
                f"Cost_per_hr must be a number e.g. 100 or 100.10")
        if not vessel_name or not vessel_name.strip():
            raise ValueError(f"Vessel name cannot be empty")
        if cost_per_hr < 1:
            raise ValueError(f"Cost_per_hr must be >= 1")

        # adding vessel to vessel table
        rows, column_names = self.vessels_table_actions.add_vessel_proc(
            vessel_name, cost_per_hr)
        # Getting the vessel id for the newly added vessel
        vessel_id = rows[0][0]

        # If the newly created vessel exists
        if vessel_id is not None:
            return rows, column_names

        return rows, column_names

    # This method displays all rows from the total revenue view.
    def get_total_rev_view(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from toal rev view
        rows, column_names = self.vessels_table_actions.get_total_rev_view()
        return rows, column_names


# This class manages TripsDal interactions
class TripService:
    def __init__(self, trips_table_actions: dal.TripsDal):
        self.trips_table_actions = trips_table_actions

    # This method gets all trips from the trip db table
    def get_all_trips(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from trip table
        rows, column_names = self.trips_table_actions.get_all_rows()
        return rows, column_names

    # This method adds a trip to the trip table
    def add_trip(self, vessel_name: str, first_name: str, last_name: str,
                 date: str, time: str, trip_length: int,
                 total_passengers: int) -> Tuple[List[Tuple], List[str]]:

        # Removing any leading or trailing white space
        parameters_to_strip = [vessel_name, first_name, last_name, date, time]
        stripped_parameters = [p.strip() for p in parameters_to_strip]

        vessel_name = stripped_parameters[0]
        first_name = stripped_parameters[1]
        last_name = stripped_parameters[2]
        date = stripped_parameters[3]
        time = stripped_parameters[4]

        # validating numeric inputs
        if not isinstance(trip_length, int):
            raise ValueError("Trip_length must be a whole number e.g. 2")
        if not isinstance(total_passengers, int):
            raise ValueError("Total_passengers must be a whole number e.g. 3")

        # validating required text inputs
        if not vessel_name:
            raise ValueError("Vessel name cannot be empty")
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not date:
            raise ValueError("Date cannot be empty")
        if not time:
            raise ValueError("Time cannot be empty")

        # Checking if vessel is already booked at this date and time
        vessel_conflicts: int = self.trips_table_actions.check_vessel_conflict(
            vessel_name, date, time
        )
        if vessel_conflicts > 0:
            raise ValueError(
                f"The vessel '{vessel_name}' is already booked on {date} at {time}."
            )

        # Checking if passenger is already booked at this date and time
        passenger_conflicts: int = self.trips_table_actions.check_passenger_conflict(
            first_name, last_name, date, time
        )
        if passenger_conflicts > 0:
            raise ValueError(
                f"Passenger {first_name} {last_name} is already booked on {date} at {time}."
            )

        # If no conflicts, call the stored procedure
        rows, column_names = self.trips_table_actions.add_trip_proc(
            vessel_name, first_name, last_name, date, time,
            trip_length, total_passengers
        )

        # If len(rows) == 0  the procedure inserted the row successfully
        if len(rows) == 0:
            rows = True
            column_names = True
            return rows, column_names

        # Handling the special codes returned by the stored procedure
        if rows[0][0] == -3:   # vessel and passenger not found
            rows = -3
            return rows, column_names
        elif rows[0][0] == -2:  # passenger not found
            rows = -2
            return rows, column_names
        elif rows[0][0] == -1:  # vessel not found
            rows = -1
            return rows, column_names
        elif rows[0][0] == 0:   # duplicate user or vessel (per your proc)
            rows = 0
            return rows, column_names

        # If none of the above, just return the raw rows and column names
        return rows, column_names

    # This method displays all rows from the trips view.
    def get_view_all_trips(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from toal rev view
        rows, column_names = self.trips_table_actions.get_all_trips_view()
        return rows, column_names


# This class manages PassengerDal interactions
class PassengerService:
    def __init__(self, passengers_table_actions: dal.PassengersDal):
        self.passengers_table_actions = passengers_table_actions

    # This method gets all passengers from the passenger db table
    def get_all_passengers(self) -> Tuple[List[Tuple], List[str]]:
        # Getting all rows from passenger table
        rows, column_names = self.passengers_table_actions.get_all_rows()
        return rows, column_names

    # This method gets the passenger id from the passenger db table
    def get_passenger_id(self, first_name: str, last_name: str) -> Tuple[List[Tuple], List[str]]:
        # Removing any leading or trailing white space
        first_name = first_name.strip()
        last_name = last_name.strip()

        # Validating inputs
        if not first_name or not first_name.strip():
            raise ValueError(f"Passenger's first name cannot be empty")
        if not last_name or not last_name.strip():
            raise ValueError(f"Passenger's last name cannot be empty")

        # Getting row id from passenger table
        rows, column_names = self.passengers_table_actions.get_passenger_id(
            first_name, last_name)
        # Getting row value from list of tuple
        passenger_id = rows[0][0]

        # If we found a passenger ID
        if passenger_id != -1:
            return rows, column_names

        # If no passenger ID found -1 will be the row value
        return rows, column_names

    # This method adds a passenger to the passenger table
    def add_passenger(self, first_name: str, last_name: str, phone: str) -> Tuple[List[Tuple], List[str]]:
        # Removing any leading or trailing white space
        first_name = first_name.strip()
        last_name = last_name.strip()
        phone = phone.strip()

        # validating inputs
        if not first_name or not first_name.strip():
            raise ValueError(f"Passenger's first name cannot be empty")
        if not last_name or not last_name.strip():
            raise ValueError(f"Passenger's last name cannot be empty")
        if not phone or not phone.strip():
            raise ValueError(f"Passenger's phone number cannot be empty")

        # adding passenger to passenger table
        rows, column_names = self.passengers_table_actions.add_passenger_proc(
            first_name, last_name, phone)
        # Getting the passenger id for the newly added passenger
        passenger_id = rows[0][0]

        # If the newly created passenger exists
        if passenger_id is not None:
            return rows, column_names

        return rows, column_names


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
