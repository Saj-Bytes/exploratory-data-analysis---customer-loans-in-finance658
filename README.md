Exploratory Data Analysis

Description:
What does it do? 
Aim of the project?
What did I learn?

Installation instructions
Packages that need to be installed:
- pyYAML: pip install PyYAML
- SQLAlchemy: pip install sqlachemy
- pandas: pip install pandas

File structure of the project
db_utils.py
- main code to connect and extract data from database
credentials.yaml
- credentials required to connect with the database


Function 1 - loading_credentials(filepath)
- loads the credentials from the 'credentials.yaml' file
- credentials allow us to connect to the db
- then load the yaml file as a dictionary


Class - RDSDatabaseConnector
    - Class contains method that will be used to initialise connection with database and extract data

- Class function 1: __init__(self, credentials)
    - initialises credentials into local variables
    - takes a dictionary of the AWS database credentials as a parameter

- Class function 2: initialise_engine(self)
    - creates a connection string required for SQLAlchemy to connect to database 
    - connection string has to be in a certain format
    - we use the create_engine() function from SQLAlchemy using the connection string to connect and manage database
    - this engine object with pandas library allows us to extract data from the database


- Class Function 3: extract_data(self, table_name)
    - takes database table_name as a parameter
    - checks if the engine object is initialised
    - engine object is required to connect to the database
    - then adds a SQL query to return all the data from the database table and uses pandas to turn it into a dataframe
    - SQL commands have to be written inside a string in python

- Class Function 4: save_data(self, df, file_path)
    - saves data from table in csv format


Function 2 - load_data_from_csv(file_path)
- Loads data from the csv file into a pandas dataframe 
- Prints shape and head of dataframe

Running db_utils.py
- using 'if __name__ == "__main__" makes sure it only runs when this file is ran, it does not if this file is imported
- loads the credentials from the YAML file
- creates a RDSDatabaseConnector object with these credentials 
- uses the intialise_engine to connect with the database on this object
- extracts the data from the table and saves into a pandas dataframe
- loads the data into a dataframe and prints some of the data

