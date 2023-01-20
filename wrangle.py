### module for functions prepare and acquire
import os
import pandas as pd
from scipy import stats
from pydataset import data
import numpy as np
import wrangle
import env
from sklearn.model_selection import train_test_split



def get_connection(db, username=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'
    '''
    this function acts as a part of the function below to establish a connection
    with the sql server
    '''
    
def get_zillow_sfr_data():
    
    '''
    this function retrieves the zillow info from the sql server
    or calls up the csv if it's saved in place
    
    '''
    
    filename = "zillow_sfr.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips FROM properties_2017 JOIN propertylandusetype USING (propertylandusetypeid) WHERE propertylandusedesc = "Single Family Residential"', get_connection ('zillow'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df
    
def train_val_test(df):
    '''
    this function splits up the data into sections for training,
    validating, and testing
    models
    '''
    seed = 99
    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed)
    
    validate, test = train_test_split(val_test, train_size = 0.5, random_state = seed)
    
    return train, validate, test

def clean_prep_zillow(df):
    df = df.dropna()
    df.drop_duplicates(inplace = True)
    df.drop([df.columns[0]], axis = 1, inplace = True)
    df.rename(columns = {'bedroomcnt' : 'bedroom',
                       'bathroomcnt': 'bathroom',
                       'calculatedfinishedsquarefeet':'sqrft',
                       'taxvaluedollarcnt':'tax_value',
                       'yearbuilt':'year_built'}, inplace = True)
    
    train, validate, test = train_val_test(df)
    
    return train, validate, test