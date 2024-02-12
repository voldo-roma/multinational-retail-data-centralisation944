import yaml

def read_db_creds():
    with open('db_creds.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials