# 09/02/2024
# create a utility class
# methods inside it will need to be fit to extract data from a particular data source, including CSV files, APIs and an S3 bucket.

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
