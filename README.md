# Exploratory Data Analysis

## Description:
- This project demonstrates how to extract and save a dataset from AWS database and load it as a pandas dataframe for Exploratary Data Analysis (EDA).
- The dataset is extracted using RDSDatabaseConnector class in db_utils.py using secret credentials. 
- The dataset is part of the repository and can be used for a further manipulation and EDA.

## Installation Instructions
To run the project locally you can clone the project using git. 

https://github.com/Saj-Bytes/exploratory-data-analysis---customer-loans-in-finance658.git


## Usage Instructions
- Once project is cloned, open in your preferred IDE e.g. VS Code 
- No need to run the db_utils.py file as AWS credentials are needed
- db_util.py only shows how to download the dataset from a AWS Database
- 'loan_payments.csv' is the file from the database, which can be explored within this repository.

---
## File Structure of the Project
1.  db_utils.py - used to connect to the AWS database and return the dataset

2. data_transform.py - 3 classes - used to apply transformations to the dataset
3. dataframe_info.py - used to help get information about the dataframe
4. eda_nb.ipynb - main file using jupyter notebook. EDA steps are explained and provides output for each step. Notebook easier to see outputs without running entire python scripts.

5. df_cleaned.pkl - Cleaned dataset after steps from 'eda_nb.ipynb' are complete.

6. loan_payments.csv - Initial dataset loaded in from AWS database

7. transformed_df.csv - Database after nulls have been removed. Before any transformations have been applied onto dataframe.


## Packages that need to be installed:
- pyYAML: pip install PyYAML
- SQLAlchemy: pip install sqlachemy
- pandas: pip install pandas
- numpy: pip install numpy
- scipy: pip install scipy
- seaborn: pip install seaborn
- plotly: pip install plotly
- statsmodels: pip install statsmodels 
- scikit-learn: pip install scikit-learn
- missingno: pip install missingno