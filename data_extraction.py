# 09/02/2024
# create a utility class
# methods inside it will need to be fit to extract data from a particular data source, including CSV files, APIs and an S3 bucket.
import tabula
import pandas as pd

class DataExtractor:
    #DataExtractor object creation
    def __init__(self, data):
        self.data = data
    #extract data from APIs
    def extract_data(self, api_url_here, params=None):
        pass
    #extract data from csv
    def extract_data(self, path_here):
        pass
    #AWS
    def extract_from_s3(self, bucket_name, file_name, aws_credentials):
        # Placeholder method for extracting data from an S3 bucket
        pass
#Step 2:
#Create a method in your DataExtractor class called retrieve_pdf_data, which takes in a link as an argument and returns a pandas DataFrame.
#Use the tabula-py Python package, imported with tabula to extract all pages from the pdf document at following link .
#Then return a DataFrame of the extracted data.
    def retrieve_pdf_data(self, link):
        try:
            # Extract data from PDF using tabula-py
            df_list = tabula.read_pdf(link, pages='all', multiple_tables=True)
            combined_df = pd.concat(df_list)
            return combined_df
        except Exception as e:
            print("Error extracting data from PDF:", str(e))
            return None

