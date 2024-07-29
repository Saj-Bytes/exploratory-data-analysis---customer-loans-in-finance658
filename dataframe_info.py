import pandas as pd

class DataframeInfo:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def describe_columns(self):
        '''Get info about the dataframe; column names, non-null values, datatypes etc '''
        print("DataFrame Info: ")
        self.df.info()

    def get_stats(self):
        ''''Different statistics about the dataframe '''
        print("\nDescriptive Statistics:")
        print(self.df.describe(include='all'))

    def get_mean(self, col_name):
        '''Get the mean of a numerical column'''
        print(f"\nMean Value of {col_name}:")
        mean_value = self.df[col_name].mean()
        print(mean_value)
        
    def get_mode(self, col_name):
        '''Get the mode of a numerical column'''
        print(f"\nMode Value of {col_name}:")
        mode_value = self.df[col_name].mode()
        print(mode_value)

    def get_median(self, col_name):
        '''Get the median of a numerical column'''
        print(f"\nMedian Value of {col_name}:")
        median_value = self.df[col_name].median()
        print(median_value)

    def unique_values(self,col_name):
        '''Get the number of unique values and the unique values of a categorical column'''
        print(f"\nNumber of unique values of {col_name}:")
        no_unique_value = self.df[col_name].nunique()
        print(no_unique_value)
        
        print(f"\nThe unique values of {col_name}:")
        unique_value = self.df[col_name].unique()
        print(unique_value)
    
    def values_count(self, col_name):
        '''Count of each unique value in a categorical column'''
        unique_count = self.df[col_name].value_counts()
        print(unique_count)

    def get_shape(self):
        '''Get the number of columns and rows of a dataframe'''
        print(f"Shape of dataframe is:")
        shape = self.df.shape
        print(shape)

    def null_percent(self):
        '''Get the percent of null values in each column'''
        print(f"Percentage of null values in each column:")
        null_values_prcnt = self.df.isna().mean()*100
        print(null_values_prcnt)

    def null_count(self):
        '''Get the count of null values in each column'''
        print(f"Count of null values in each column:")
        null_values_count = self.df.isna().sum()
        print(null_values_count)

    def null_columns_info(self):
        '''Gives a summary of ONLY columns that contain null values and the percentage of null values in each'''
        #Number of null values per column
        null_count = self.df.isnull().sum()

        #Percentage of null values 
        null_percent = (null_count / len(self.df))*100

        #Columns with at least one null value
        columns_with_null = null_percent[null_percent>0]

        #dataframe with columns and their null %
        nulls_df = columns_with_null.reset_index()
        nulls_df.columns = ['Column', "| % of Null values"]

        print(nulls_df)

    def columns_with_null(self):
        '''Shows column names with nulls'''
        columns_with_null = self.df.columns[self.df.isnull().any()]
        print(columns_with_null)


    def count_specific_value(self,col_name, value):
        '''Counts the number of times a specific value occurs in a column'''
        value_counts = self.df[col_name].value_counts()

        try: 
            specific_value = value_counts[value]
            print(f'Count of value {value}:', specific_value)
        except Exception:
            print(f"Value {value} is not found")

    def rows_with_null(self, col_name):
        '''Returns the specific rows that have null values'''
        print(self.df[self.df[col_name].isnull()][col_name])


    def get_columns_by_dtype(self, dtype):
        '''Returns column names of a specific data type'''
        return self.df.select_dtypes(include=[dtype]).columns.tolist()

    

 

        



        

        

    
    


        
