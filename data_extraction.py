import pandas as pd
from database_utils import DatabaseConnector
class DataExtractor:
    def __init__(self, data=None):
        self.data = data

    # Existing methods...

    def read_rds_table(self, db_connector, table_name):
        """
        Extracts a table from the RDS database into a pandas DataFrame.

        :param db_connector: An instance of DatabaseConnector
        :param table_name: The name of the table to extract
        :return: A pandas DataFrame containing the table's data
        """
        # Use the db_connector to get an SQLAlchemy engine
        engine = db_connector.init_db_engine()
        if engine is not None:
            # Use pandas to read the SQL table directly into a DataFrame
            try:
                df = pd.read_sql_table(table_name, con=engine)
                return df
            except Exception as e:
                print(f"Error reading table {table_name}: {e}")
                return pd.DataFrame()  # Return an empty DataFrame in case of error
        else:
            print("Failed to connect to the database.")
            return pd.DataFrame() 
#%%