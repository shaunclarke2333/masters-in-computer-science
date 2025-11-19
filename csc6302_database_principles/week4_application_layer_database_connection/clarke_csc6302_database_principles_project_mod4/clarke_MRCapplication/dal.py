"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 04: Application Layer
"""

import mysql.connector
import pandas as pd
from typing import List, Tuple


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

    # This method handles converting the SQL output to a dataframe
    def make_dataframe(self, rows: List, column_names: List) -> str:
        """
        - Converts query output to a dataframe.
        - returns a str.
        """
        # Using pandas to convert data to dataframe, also using to string method to remove index.
        df = pd.DataFrame(rows, columns=column_names).to_string(
            index=False, justify='center')

        return df

    # This method performs a select query
    def select_query(self, query: str, params: tuple | None = None) -> str:
        """
        - This method runs select queries(Select, functions, views etc).
        - returns a str.
        """
        # Executing query
        self._cursor.execute(query, params)
        # Getting rows and column headers from output
        column_names: List = self._cursor.column_names
        rows: List = self._cursor.fetchall()

        return rows, column_names

    # This method handles procedure calls
    def procedure_calls(self, proc_name: str, params: Tuple | None = None) -> str:
        self._cursor.callproc(proc_name, params)

        # Lists for rows and columns data
        rows = []
        column_names = []

        # parsing output to get rows and columns headers
        for results in self._cursor.stored_results():
            column_names: List = results.column_names
            rows: List = results.fetchall()

        # Converting output to readable format
        output = self.make_dataframe(rows, column_names)
        return rows, column_names

    def commit(self):
        self._db.commit()


# This class handles interaction with the vessels table
class VesselsTable:
    def __init__(self, database_action_object: DatabaseActions):
        self._db_actions = database_action_object

    # This method returns all rows from vessles table
    def get_all_rows(self) -> str:
        # getting all rows from the vessel table
        query_output = self._db_actions.select_query("SELECT * FROM vessels")
        return query_output

    # This method calls the get vesssel ID function
    def get_vessel_id(self, vessel_name: str) -> str:
        func_params = (vessel_name,)
        # Calling the vessel ID function
        rows, column_names = self._db_actions.select_query(
            "SELECT getVesselID(%s)", func_params)
        return rows, column_names

    # This procedure adds a vessel to the vessels table
    def add_vessel(self, vessel_name: str, cost_per_hr: int) -> str:
        proc_params = (vessel_name, cost_per_hr)
        # calling the add vessel procedure
        rows, column_names = self._db_actions.procedure_calls(
            "addVessel", proc_params)
        # Commiting chnages to DB
        self._db_actions.commit()
        return rows, column_names


# This class handles interaction with the passengers table


# This class handles interaction with the trips table

if __name__ == "__main__":
    try:
        connection = ManageDbConnection(
            host="localhost",
            user="root",
            port=3306,
            database="mrc",
            password="N@thin23"
        )

        connection.connect_to_db()
        db_actions = DatabaseActions(connection)

        vessels = VesselsTable(db_actions)

        rows, cols = vessels.get_vessel_id("Ocean Voyager")
        print(pd.DataFrame(rows, columns=cols).to_string(
            index=False, justify='center'))

        rows, cols = vessels.add_vessel("Sea Breeze", 100)
        print(pd.DataFrame(rows, columns=cols).to_string(
            index=False, justify='center'))

        rows, cols = vessels.get_all_rows()
        print(pd.DataFrame(rows, columns=cols).to_string(
            index=False, justify='center'))

    except mysql.connector.Error as err:
        print("Database error:", err)
