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
    #specify a credentials file path
    def __init__(self, creds_file="db_creds.yaml"):
        self.creds_file = creds_file
    # Read database credentials from a YAML file, ensuring that sensitive info is not hardcoded
    def read_db_creds(self, file_path="db_creds.yaml"):
        with open(file_path, "r") as file:
            creds = yaml.safe_load(file)    
        return creds
    # Initialize the engine
    def init_db_engine(self):
        creds = self.read_db_creds()  # This should call the read_db_creds method
        try:
            engine = create_engine(f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
            return engine
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None
    #list the tables in the database
    def list_db_tables(self):
        engine = self.init_db_engine()
        if engine is not None:
            inspector = inspect(engine)
            return inspector.get_table_names()
        else:
            print("Failed to connect to database.")
            return []
    def upload_to_db(self, dataframe, table_name):
        engine = self.init_db_engine()
        if engine is not None:
            try:
                dataframe.to_sql(name=table_name, con=engine, if_exists='append', index=False)
                print(f"Data uploaded successfully to {table_name}.")
            except Exception as e:
                print(f"Error uploading data to the database: {e}")
        else:
            print("Database engine is not initialized.")
database_connector = DatabaseConnector()
engine = database_connector.init_db_engine()
if engine is not None:
    print("Connection is on.")
    print("RDS_HOST: data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com")
    print("RDS_USER: aicore_admin")
    print("RDS_PASSWORD: *********")
else:
    print("Failed to establish connection to the RDS.")