"""
Author: Shaun Clarke
Class: CSC6302 Database Principles
Module 04: Application Layer
"""

import mysql.connector
from typing import List, Dict, Tuple


# This class manages the database connection
class ManageDbConnection:
    def __init__(self, host: str, user: str, port: int, database: str, password: str):
        self.__host = host
        self.__user = user
        self.__port = port
        self.__database = database
        self.__password = password
        self.__db_object = None
        self.__cursor = None
        self.__is_connected: bool = False
        self.__has_cursor: bool = False

    # This method connects to the database
    def __connect_to_db(self):
        """
        - This method conects to the specified DB.
        """

        try:
            # Establishing DB connection with params
            self.__db_object = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                port=self.__port,
                database=self.__database,
                password=self.__password
            )

            # Creating Cursor
            self.__cursor = self.__db_object.cursor()
            # Setting cursor and connection status
            self.__has_cursor = True
            self.__is_connected = True
        except mysql.connector.Error as err:
            raise mysql.connector.Error(err)
        
    # This method gets the DB connection
    def get_connection(self) -> object:
        # if database is not connected, connect it and return the DB object
        if self.__is_connected:
            return self.__db_object
        else:
            # Connecting DB
            self.__connect_to_db()
            return self.__db_object
        
    # This method gets the cursor
    def get_cursor(self) -> object:
        # If the there is no cursor create one
        if self.__has_cursor and self.__is_connected:
            return self.__cursor
        elif not self.__has_cursor and self.__is_connected:
            self.__cursor = self.__db_object.cursor()
            self.__has_cursor = True
            return self.__cursor
        elif not self.__has_cursor and not self.__is_connected:
            # Connect to DB
            self.__connect_to_db()
            # Create cursor
            self.__cursor = self.__db_object.cursor()
            # update cursor status
            self.__has_cursor = True
            
            return self.__cursor
    
    # This method gets cursor status
    def get_cursor_status(self):
        return self.__has_cursor

    # This method gets connections status
    def get_connection_status(self):
        return self.__is_connected

    # This method closes the cursor
    def close_cursor(self):
        """
        - This method closes the cursor.
        - returns nothing.
        """
        if self.__cursor is not None:
            self.__cursor.close()
            # Setting cursor object to None to cleanup cursor connection
            self.__cursor = None
            # Updating cursor status
            self.__has_cursor = False

    # This method closes the db connection
    def close_db_connection(self):
        """
        - This method closes the DB connection.
        - returns nothing.
        """
        # if the DB object is present close it
        if self.__db_object is not None:
            self.__db_object.close()
            # Setting database object to None to cleanup closed connection
            self.__db_object = None
            # Updating DB connection status
            self.__is_connected = False

# This class manages the database crud actions
class DatabaseActions:
    def __init__(self, connection: ManageDbConnection):
        self.__connection = connection  # The database connection instance

    # Select Query
    def select_query(self, query: str, params: tuple | None = None) -> List[Tuple]:
        db = self.__connection.get_connection()
        cursor = self.__connection.get_cursor()
        cursor.execute(query, params)
        output = cursor.fetchall()

        cursor.callproc("getPassengerList")
        for results in cursor.stored_results():
            print(results.fetchall())

        self.__connection.close_cursor()
        if not self.__connection.get_cursor_status():
            print(f"DB cursor closed")

        self.__connection.close_db_connection()
        if not self.__connection.get_connection_status():
            print(f"DB connection closed")
        
        return output





if __name__ == "__main__":

    try:
        # Below this line is for testing as i build
        connection = ManageDbConnection(
            host="localhost",
            user="root",
            port=3306,
            database="mrc",
            password="N@thin23"

        )

        db_actions = DatabaseActions(connection)

        output = db_actions.select_query("SELECT * FROM vessels")
        for data in output:
            print(data)

        # db = connection.get_connection()
        # cursor = connection.get_cursor()

        # print(type(db))
        # print(type(cursor))

        # print(f"DB connected successfully\n")

    except mysql.connector.Error as err:
        print(err)
        exit(1)

    # cursor.execute(
    #     """
    # SELECT
    #     *
    # FROM
    #     passengers

    # """
    # )

    # for data in cursor:
    #     print(data)

    # cursor.execute("SHOW TABLES")
    # for data in cursor:
    #     print(data)

    # connection.close_cursor()
    # if not connection.get_cursor_status():
    #     print(f"DB cursor closed")

    # connection.close_db_connection()
    # if not connection.get_connection_status():
    #     print(f"DB connection closed")
