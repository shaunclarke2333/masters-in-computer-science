


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