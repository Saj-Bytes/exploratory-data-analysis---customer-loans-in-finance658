import yaml
import pandas as pd
from sqlalchemy import create_engine

def loading_credentials(filepath):
    with open(filepath, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


class RDSDatabaseConnector:
    ''' Initialise connection with database '''
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.engine = None

    #Step 5    
    def initialise_engine(self):
        ''' Uses a connection string that SQLAlchemy uses to connect to the db '''
        connection_string = (
            f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )
        self.engine = create_engine(connection_string)
        print("Engine initialised")

    #Step 6
    def extract_data(self, table_name):
        ''' Extracts data from the db and returns as a df '''
        if self.engine is None:
            self.initialise_engine()

        query = f"SELECT * FROM {table_name}"

        df = pd.read_sql(query, self.engine)
        return df


    #Step 7
    def save_data(self, df, file_path):
        ''' Saves data to local machine in csv format '''
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")


def load_data_from_csv(file_path):
    ''' Load data from local csv file into pandas df '''
    df = pd.read_csv(file_path)
    print(f"Data shape: {df.shape}")

    print(f"Data sample: \n{df.head}")

    return df


if __name__ == "__main__": 
    creds = loading_credentials('credentials.yaml')
    connector = RDSDatabaseConnector(creds)
    connector.initialise_engine()
    df = connector.extract_data('loan_payments')
    connector.save_data(df, 'loan_payments.csv')
    print("Data extraction and saving completed")

    data_frame = load_data_from_csv('loan_payments.csv')




