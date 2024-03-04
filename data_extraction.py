# packages first to be imported
import pandas as pd
import requests #for HTTP requests to API
from database_utils import DatabaseConnector #for database ops
from io import StringIO #in-memory file ops
import boto3 #for interaction with AWS services

# create main classes
class DataExtractor:
    def __init__(self, data=None):
        self.data = data
################################################################
    #METHODS:    
    # Makes an API call to retrieve the number of stores, includes error handling.
    def list_number_of_stores(self, endpoint, headers):
            response = requests.get(endpoint, headers=headers)
            if response.status_code == 200:
                return response.json()['number_of_stores']
            else:
                print("Failed to retrieve the number of stores")
                return 0
    # iterates over store numbers, make API calls for each store, returns a df containing all stores' data.
    def retrieve_stores_data(self, base_endpoint, headers):
        number_of_stores = self.list_number_of_stores(base_endpoint + "/number_stores", headers)
        stores_data = []
        for store_number in range(1, number_of_stores + 1):
            store_response = requests.get(f"{base_endpoint}/store_details/{store_number}", headers=headers)
            if store_response.status_code == 200:
                stores_data.append(store_response.json())
        return pd.DataFrame(stores_data)
    # Uses DatabaseConnector to create a connection to an RDS database and extract a specified table into a df. Includes error handling for connection and reading issues.
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
    # Extracts extracts the S3 bucket name and key, uses boto3 to retrieve the object, and reads it into a df.
    #%%
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
    #%%
    # Instantiate the DataExtractor class
extractor = DataExtractor()

# Define the S3 URI of the CSV file you want to extract
s3_uri = "s3://data-handling-public/products.csv"
# Call the method and get the DataFrame
products_df = extractor.extract_from_s3(s3_uri)

# Now 'products_df' is a pandas DataFrame containing the data from the 'products.csv' file
print(products_df.head())  # Display the first few rows of the DataFrame

    #%%
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
# %%
