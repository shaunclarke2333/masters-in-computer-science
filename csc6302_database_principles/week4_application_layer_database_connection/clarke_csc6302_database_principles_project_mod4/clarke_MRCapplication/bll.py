"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 04: Application Layer
"""

from typing import List, Tuple
import dal


# Creating database Object
connection = dal.ManageDbConnection(
    host="localhost",
    user="root",
    port=3306,
    database="mrc",
    password="N@thin23"
)

# Connecting database
connection.connect_to_db()

# Instantiating database actions object
db_actions = dal.DatabaseActions(connection)

# Instantiating Dal table instances
vessels_table_actions = dal.VesselsDal(db_actions)
trips_table_actions = dal.TripsDal(db_actions)
passengers_table_actions = dal.PassengersDal(db_actions)


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
        vessel_name.strip()
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
    def add_trip(self, vessel_name: str, first_name: str, last_name: str, date: str, time: str,
                 trip_length: int, total_passengers: int) -> Tuple[List[Tuple], List[str]]:

        # Removing any leading or trailing white space
        parameters_to_strip = [vessel_name, first_name,
                               last_name, date, time]
        # List of stripped parameters
        stripped_parameters = [p.strip() for p in parameters_to_strip]

        vessel_name = stripped_parameters[0]
        first_name = stripped_parameters[1]
        last_name = stripped_parameters[2]
        date = stripped_parameters[3]
        time = stripped_parameters[4]

        # validating inputs
        if not isinstance(trip_length, int):
            raise ValueError(
                f"Trip_length must be a whole number e.g.2 ")
        if not isinstance(total_passengers, int):
            raise ValueError(
                f"Total_passengers must be a whole number e.g. 3")
        if not vessel_name:
            raise ValueError(f"Vessel name cannot be empty")
        if not first_name:
            raise ValueError(f"First name cannot be empty")
        if not last_name:
            raise ValueError(f"Last name cannot be empty")
        if not date:
            raise ValueError(f"Date name cannot be empty")
        if not time:
            raise ValueError(f"Time name cannot be empty")

        # adding trip to trip table
        rows, column_names = self.trips_table_actions.add_trip_proc(
            vessel_name, first_name, last_name, date, time, trip_length, total_passengers)
        # Getting the trip id for the newly added trip
        trip_id = rows[0][0]

        # If the newly created trip exists
        if trip_id is not None:
            return rows, column_names

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
        first_name.strip()
        last_name.strip()

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
        phone.strip()

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
class ServiceManager:
    def __init__(self):
        pass
