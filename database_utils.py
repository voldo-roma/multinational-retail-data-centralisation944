import yaml
#Create another script named database_utils.py and within it, create a class DatabaseConnector which you will use to connect with and upload data to the database.
class DatabaseConnector:
    def read_db_creds(self):
        with open("db_creds.yaml", "r") as file:
            return yaml.safe_load(file)