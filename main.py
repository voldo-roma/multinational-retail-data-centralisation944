from data_extraction import DataExtractor
from database_utils import DatabaseConnector
from data_cleaning import DataCleaning

# Example usage
if __name__ == "__main__":
    # Extract data from RDS database
    db_connector = DatabaseConnector()
    extractor = DataExtractor()
    tables = db_connector.list_db_tables()
    if "user_data" in tables:
        user_data = extractor.read_rds_table(db_connector, "user_data")
        cleaned_user_data = DataCleaning.clean_user_data(user_data)
        
        # Upload cleaned user data to database
        db_connector.upload_to_db(cleaned_user_data, "dim_users")
    else:
        print("User data table not found in the database.")
