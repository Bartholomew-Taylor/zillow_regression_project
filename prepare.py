import os
import pandas as pd
from scipy import stats
from pydataset import data
import numpy as np
import wrangle
import env
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler



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
    df.drop(columns = ['transactiondate'], inplace = True)
    for col in df:
        
        mean = df[col].mean()
        sd = df[col].std()
        
        df = df[(df[col] <= mean+(5*sd))]
    
    train, validate, test = train_val_test(df)
    
    return train, validate, test

def modeling_split(intrain, inval, intest, target):
    '''
    this func splits the train, val, and test sets 
    into x and y for modeling input
    
    ** target must be input as string **
    '''
    
    x_train = intrain.drop(columns = [target], axis = 1)
    y_train = intrain[target]
    x_val = inval.drop(columns = [target], axis = 1)
    y_val = inval[target]
    x_test = intest.drop(columns = [target], axis = 1)
    y_test = intest[target]
    
    return x_train, y_train, x_val, y_val, x_test, y_test

def dummy_scale(df, train_df):
    
    '''
    this function generates scaled sqrft and creates dummy
    columns for modeling
    '''
    
    df['year_bin'] = pd.qcut(df['year_built'], 10, labels = ['a','b','c','d','e','f',
                                                          'g','h','i','j'])
    
    df = pd.get_dummies(df, columns = ['bedroom','bathroom','fips','year_bin'], 
                             drop_first = [True, True])   
    
    mm_scaler = MinMaxScaler()
    mm_scaler.fit(train_df[['sqrft']])
    sqft_scaled = mm_scaler.transform(df[['sqrft']])
    df['sqft_scaled'] = sqft_scaled
    df.drop(columns = ['sqrft','year_built'], inplace = True)
    
    return df



def prep_2_model(xtr, xv, xtt, train_df):
    oxtr = dummy_scale(xtr, train_df)
    oxv = dummy_scale(xv, train_df)
    oxtt = dummy_scale(xtt, train_df)
    oxtr.drop(columns = ['year_bin_j','year_bin_c','bedroom_4.0','fips_6111.0','year_bin_b','bathroom_2.0'], 
        inplace = True)
    oxv.drop(columns = ['year_bin_j','year_bin_c','bedroom_4.0','fips_6111.0','year_bin_b','bathroom_2.0'], 
        inplace = True)
    oxtt.drop(columns = ['year_bin_j','year_bin_c','bedroom_4.0','fips_6111.0','year_bin_b','bathroom_2.0'], 
        inplace = True)
    return oxtr, oxv, oxtt

