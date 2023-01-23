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
        df = pd.read_sql("SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, fips, transactiondate FROM properties_2017 JOIN propertylandusetype USING (propertylandusetypeid) JOIN predictions_2017 USING (id) WHERE propertylandusedesc = 'Single Family Residential' HAVING transactiondate BETWEEN '2017-01-01' AND '2017-12-31' ", get_connection ('zillow'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df