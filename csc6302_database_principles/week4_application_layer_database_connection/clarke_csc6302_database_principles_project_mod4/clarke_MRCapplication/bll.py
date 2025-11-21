"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 04: Application Layer
"""

import pandas as pd
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
connection.connect_to_db

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

        # Making sure vessel_name is not empty
        if vessel_name is not None and len(vessel_name) > 1:
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
    def add_vessel(self, vessel_name: str, cost_per_hr: int):

        # Making sure we don't have any null values
        if vessel_name is not None and cost_per_hr >= 1:
            # adding vessel to vessel table
            rows, column_names = self.vessels_table_actions.add_vessel_proc(vessel_name, cost_per_hr)
            # Getting the vessel id for the newly added vessel
            vessel_id = rows[0][0]

            # If the newly created vessel exists
            if vessel_id != None:
                return rows, column_names
            
            return rows, column_names
        
    
    # This method displays all rows from the total revenue view.
    def get_total_rev_view(self):
        # Getting all rows from toal rev view
        rows, column_names = self.vessels_table_actions.get_total_rev_view()
        return rows, column_names




# This class manages TripsDal interactions
class TripService:
    def __init__(self):
        pass

# This class manages PassengerDal interactions


class PassengerService:
    def __init__(self):
        pass

# This class manages the interaction between the view and Dal


class ServiceManager:
    def __init__(self):
        pass
