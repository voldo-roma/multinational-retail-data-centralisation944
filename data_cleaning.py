#%%
import pandas as pd
class DataCleaning:
    # method for cleaning data extracted from CSV file
    def clean_user_data(self, df):
            
    # clean_user_data method in the DataCleaning class (takes )
        try:
            # Remove any rows with NULL values
            df_cleaned = df.dropna()
            # Remove erroneous values or errors with formatting (customize as needed)
            # Example: Remove rows where the 'Amount' column is negative
            df_cleaned = df_cleaned[df_cleaned['Amount'] >= 0]
            return df_cleaned
        except Exception as e:
            print("Error cleaning data:", str(e))
            return None    
    
