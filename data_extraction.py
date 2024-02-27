# packages first to be imported
import pandas as pd
import requests
from database_utils import DatabaseConnector
from io import StringIO
import boto3

# create main classes
class DataExtractor:
    def __init__(self, data=None):
        self.data = data

    # Existing methods...
    def list_number_of_stores(self, endpoint, headers):
            response = requests.get(endpoint, headers=headers)
            if response.status_code == 200:
                return response.json()['number_of_stores']
            else:
                print("Failed to retrieve the number of stores")
                return 0
    def retrieve_stores_data(self, base_endpoint, headers):
        number_of_stores = self.list_number_of_stores(base_endpoint + "/number_stores", headers)
        stores_data = []
        for store_number in range(1, number_of_stores + 1):
            store_response = requests.get(f"{base_endpoint}/store_details/{store_number}", headers=headers)
            if store_response.status_code == 200:
                stores_data.append(store_response.json())
        return pd.DataFrame(stores_data)
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
    # Extract data from S3 bucket and return it as a pandas DataFrame
    def extract_from_s3(self, s3_uri):
        # Parse the S3 URI
        bucket_name = s3_uri.split('/')[2]
        key = '/'.join(s3_uri.split('/')[3:])
        
        # Initialize S3 client
        s3 = boto3.client('s3')
        
        # Get the object from S3
        response = s3.get_object(Bucket=bucket_name, Key=key)
        
        # Read the object's content into pandas DataFrame
        content = response['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(content))
        
        return df
# tests
if __name__ == "__main__":
    headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
    base_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod"

    extractor = DataExtractor()
    number_of_stores = extractor.list_number_of_stores(f"{base_endpoint}/number_stores", headers)
    print(f"Number of stores: {number_of_stores}")

    if number_of_stores > 0:
        stores_data_df = extractor.retrieve_stores_data(base_endpoint, headers)
        print(stores_data_df.head())