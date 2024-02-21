#
import yaml
from sqlalchemy import create_engine
#Create another script named database_utils.py and within it, create a class DatabaseConnector which you will use to connect with and upload data to the database.
class DatabaseConnector:
    def read_db_creds(self):
        with open("db_creds.yaml", "r") as file:
            creds = yaml.safe_load(file)    
        return creds

def init_db_engine(self, credentials):
    try:
        # Create a connection to the database
        engine = create_engine("mysql+pymysql://" + credentials['user'] + ":" + credentials['password'] + "@" + credentials['host'] + ":" + credentials['port'] + "/" + credentials['database'])
        return engine
    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None