# explorer stuff for zillow
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
import pandas as pd
from scipy import stats
from pydataset import data
import numpy as np
import env
import matplotlib.pyplot as plt
import os
import prepare
import wrangle
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
import explore


def plot_variable_pairs(dfi):
    dfi = dfi.drop(columns = ['fips'])
    sns.pairplot(dfi.sample(1000), kind="reg", plot_kws={'line_kws':{'color':'red'}})
    plt.show()
    return dfi

def plot_categorical_and_continuous(dfi, cat, cont):
    datain = dfi.sample(1000)
    sns.boxplot(x= dfi[cat], y= dfi[cont], data=datain)
    plt.show()
    sns.violinplot(x= dfi[cat], y= dfi[cont], data=datain)
    plt.show()
    sns.barplot(x= dfi[cat], y= dfi[cont], data=datain)
    plt.show()
    return dfi