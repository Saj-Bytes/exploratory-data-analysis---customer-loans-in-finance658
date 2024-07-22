import yaml
import pandas as pd
from sqlalchemy import create_engine

#we will initialise the class and script that you will use to extract the data from the cloud

def loading_data(filepath):
    with open(filepath, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


#This class will contain the methods to extract data from the RDS Database
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.engine = None

    #Step 5    
    def initialise_engine(self):
        '''
        Uses a connection string that SQLAlchemy uses to connect to the db
        '''
        connection_string = (
            f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

        #  Create_engine function used from SQLAlchemy to create
        #  an engine object
        #  SQLAlchemy uses this to manage the connections to the DB
        #  using connection string, it connects to the db
        self.engine = create_engine(connection_string)
        print("Engine initialised")

    #Step 6
    def extract_data(self, table_name):
        '''
        extracts data from the db and returns as a df
        '''
        #Checks if the engine is intialised
        #engine object required to connect to the db
        if self.engine is None:
            self.initialise_engine()

        #SQL query to get all data from the table
        #SQL commands written as string in python
        query = f"SELECT * FROM {table_name}"

        #use pandas to execute the query & get the data into a df
        df = pd.read_sql(query, self.engine)
        return df


    #Step 7
    def save_data(self, df, file_path):
        '''
        Saves data to local machine in csv format
        '''
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")


if __name__ == "__main__": #only runs if file is ran, not when imported
    creds = loading_data('credentials.yaml')
    connector = RDSDatabaseConnector(creds)
    connector.initialise_engine()
    df = connector.extract_data('loan_payments')
    connector.save_data(df, 'loan_payments.csv')
    print("Data extraction and saving completed")




def load_data_from_csv(file_path):
    '''
    Load data from local csv file into pandas df
    '''

    df = pd.read_csv(file_path)
    print(f"Data shape: {df.shape}")

    print(f"Data sample: \n{df.head}")

    return df

if __name__ == "__main__":
    data_frame = load_data_from_csv('loan_payments.csv')


        