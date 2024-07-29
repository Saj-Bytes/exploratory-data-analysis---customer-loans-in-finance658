import numpy as np
import pandas as pd
import missingno
import seaborn as sns
from scipy.stats import normaltest, yeojohnson
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from sklearn.preprocessing import LabelEncoder



class ChangeDataType:
    
    '''Changes the datatypes of the columns to a chosen datatype '''
    def __init__(self, dataframe):
        self.df = dataframe

    def to_float(self, col_name):
        self.df[col_name] = self.df[col_name].astype('float64') 
        return self.df 

    #only when there are no null/missing values
    def to_int(self, col_name):
        self.df[col_name] = self.df[col_name].astype('int64') 
        return self.df 

    def to_category(self, col_name):
        self.df[col_name] = self.df[col_name].astype('category')
        

    def to_numeric(self, col_name):
        self.df[col_name] = pd.to_numeric(self.df[col_name])
        return self.df 

    def to_datetime(self, col_name):
        self.df[col_name] = pd.to_datetime(self.df[col_name])
        return self.df 
    
    #converts null values to NaN
    def to_numeric(self, col_name):
        self.df[col_name] = pd.to_numeric(self.df[col_name])
        return self.df 

    def drop_rows_with_null(self, col_name ):
        '''drops rows with nulls from a specific column'''
        self.df.dropna(subset=[col_name], inplace=True)



class DataFrameTransform:
    
    def __init__ (self, dataframe):
        self.df = dataframe

    def data_impute(self, col_name, method):
        '''Impute Mean, median, Mode into data'''
        if method == 'mean':
            self.df[col_name].fillna(
                self.df[col_name].mean(), inplace=True)
        elif method == 'median':
            self.df[col_name].fillna(
                self.df[col_name].median(), inplace=True)
        elif method == 'mode':
            self.df[col_name].fillna(
                self.df[col_name].mode().iloc[0], inplace=True)
        else:
            print('Invalid imputation method.')
        return self.df
        





class Plotter:

    def __init__(self, dataframe):
        self.df = dataframe
    

    def dagostino_test(self, col_name):
        '''
        Method to perform D'Agostino's K^2 test. The test provide the 
        probability that null hypothesis is false, given the data sample provided.
        The probability estimate - p-value close to 0 means data are normally distributed.
        '''
        data = self.df[col_name]
        stat, p = normaltest(data, nan_policy='omit')
        print('Statistics = %.3f, p=%.3f' % (stat, p))

   
    def yj_transform(self, col_name):
        '''Apply Yeo-Johnson method for solving positive skewness '''
        yj_transform = self.df[col_name]
        yj_transform = yeojohnson(yj_transform)
        yj_transform = pd.Series(yj_transform[0])
        self.df[col_name] = yj_transform

    def skewness(self):
        '''Print the skew value of the dataframe'''
        print(self.df.skew(numeric_only=False))

    def histogram(self, col_name, bins):
        '''
        Histogram that takes two arguments.
        column_name: which is a column name of pandas dataframe
        bins: number of bins the histogram will show of the column
        '''
        plt.hist(self.df[col_name], bins=bins)
        plt.show()

    def qq_plot(self, col_name):
        '''
        qq_plot to display values distribution of the colum.
        column_name: column name of pandas dataframe
        '''
        qq_plot = qqplot(self.df[col_name], scale=1, line='q')
        plt.show()

    def missing_values_bar(self):
        '''Bar graph to visualise distribution of values in a dataframe'''
        missingno.bar(self.df)
   
    def boxplot(self, col_name, number_of_var=0):
        '''
        Method for visualising box plot of a pandas dataframe
        If a list of columns is passed, number_of_var in the columns has to be passed 
        to display boxplots for all the var
        If only single column is passed as the argument a single boxplot is displayed.
        '''
        if number_of_var > 0:
            for i in range(number_of_var):
                self.df.boxplot(col_name[i])
                plt.show()
        else:
            self.df.boxplot(col_name)
    


    



    


    

