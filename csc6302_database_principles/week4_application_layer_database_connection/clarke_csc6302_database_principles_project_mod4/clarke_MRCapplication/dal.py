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
        self.db_object = None  # Placeholder variable that will be used for the connector object
        self.db_cursor = None  # Placeholder variable that will be used for the cursor
        self.db_connection_status = None  # Placeholder for db connection status
        self.db_closed_status = None

    # This method connects to the database
    def connect_to_db(self) -> bool:

        try:
            # Establishing DB connection with params
            self.db_object = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                port=self.__port,
                database=self.__database,
                password=self.__password
            )

            # Creating db cursor
            self.db_cursor = self.db_object.cursor()

            # Providinf connections status
            self.db_connection_status = True

            # returning the db object and conection status
            return self.db_object, self.db_cursor, self.db_connection_status

        except:
            # Providing connections status
            self.db_connection_status = False

            return self.db_connection_status

    # This method closes the db connection
    def close_db_connection(self) -> bool:
        try:
            # if the DB object is present close it
            if self.db_object is not None:
                self.db_object.close()
                self.db_closed_status = True
                return self.db_closed_status
        except:
            # If the connection was not closed return false.
            self.db_closed_status = False
            return self.db_closed_status


connection = ManageDbConnection(
    host="localhost",
    user="root",
    port=3306,
    database="mrc",
    password="N@thin23"

)

db, cursor, conn_status = connection.connect_to_db()

print(conn_status)
print(type(cursor))
cursor.execute(
    """
SELECT
    *
FROM
    passengers

"""
)

for data in cursor:
    print(data)
connection.close_db_connection()


# try:
#     # This class manages the
#     db: List = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         port=3306,
#         database="mrc",
#         password="N@thin23"
#     )


# except:
#     print(f"Database was not connected")


# db_cursor: object = db.cursor()

# db_cursor.execute(
#     """
# SELECT
#     *
# FROM
#     passengers

# """
# )

# for dbase in db_cursor:
#     print(dbase)

# if "db" in locals() and db_cursor is not None:
#     db.close()
#     print(f"MSQL connection closed")
# else:
#     print(f"Connection was already closed")
