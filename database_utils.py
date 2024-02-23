import yaml
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text
import pandas as pd

# use Properties section in pgAdmin to get the details
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'Jenkins09'
DATABASE = 'sales_data'
PORT = 5436
#Create another script named database_utils.py and within it, create a class DatabaseConnector which you will use to connect with and upload data to the database.
class DatabaseConnector:
    # Read database credentials from a YAML file, ensuring that sensitive info is not hardcoded
    def read_db_creds(self, file_path="db_creds.yaml"):
        with open(file_path, "r") as file:
            creds = yaml.safe_load(file)    
        return creds
    def init_db_engine(self):
        creds = self.read_db_creds()  # This should call the read_db_creds method
        try:
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}")
            return engine
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None
    def list_db_tables(self):
        engine = self.init_db_engine()  # Assuming you've corrected init_db_engine as suggested
        if engine is not None:
            inspector = inspect(engine)
            return inspector.get_table_names()
        else:
            print("Failed to connect to database.")
            return []
    
