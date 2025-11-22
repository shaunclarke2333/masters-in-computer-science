
import pandas as pd
from typing import List, Tuple
import dal
import bll



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


# This method handles converting the SQL output to a dataframe
def make_dataframe(rows: List, column_names: List) -> str:
    """
    - Converts query output to a dataframe.
    - returns a str.
    """
    # Using pandas to convert data to dataframe, also using to string method to remove index.
    df = pd.DataFrame(rows, columns=column_names).to_string(
        index=False, justify='center')


    return df


# Testing Vessel Service
vessel_table_service = bll.VesselService(vessels_table_actions)
rows, column_names = vessel_table_service.get_all_vessels()

print(make_dataframe(rows, column_names))

rows, column_names = vessel_table_service.get_vessel_id("Ocean Voyager")
print(make_dataframe(rows, column_names))

try:
    rows, column_names = vessel_table_service.add_vessel("jabbas", "150")
    print(make_dataframe(rows, column_names))
except Exception as err:
    print(err)

rows, column_names = vessel_table_service.get_total_rev_view()
print(make_dataframe(rows, column_names))

# Testing Trip service
trips_table_service = bll.TripService(trips_table_actions)

rows, column_names = trips_table_service.get_all_trips()
print(make_dataframe(rows, column_names))

# try:
rows, column_names = trips_table_service.add_trip("Wave Rider", "Barry", "Allen", "2025-06-30", "12:00:00", 3, 5)
print(make_dataframe(rows, column_names))
# except Exception as err:
#     print(err)

rows, column_names = trips_table_service.get_view_all_trips()
print(make_dataframe(rows, column_names))



# Testing passenger service
passenger_table_service = bll.PassengerService(passengers_table_actions)

rows, column_names = passenger_table_service.get_all_passengers()
print(make_dataframe(rows, column_names))

rows, column_names = passenger_table_service.add_passenger("Shaun", "Clarke", "212-325-4455")
print(make_dataframe(rows, column_names))

rows, column_names = passenger_table_service.get_passenger_id("Shaun", "Clarke")
print(make_dataframe(rows, column_names))

