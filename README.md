# zillow_regression_project
This the regression project utilizing the Zillow set
## Project Goals
### Utilizing data exploration and regression modeling, provide direction and recommendations concerning our target variable: Taxable Value
## Project Description
### 2017 Property data from the SQL database was filtered for Single Family Homes and specifically transactions that occured in 2017
### By creating a model that can better inform us about Taxable Value of Properties we can better serve our customers, increase copoerate credibility, and better prepare for unexpected changes in the housing market

## Project Plan
### Acquire Data
#### SQL Query
### Prepare Data
#### elmination of nulls
#### correction of naming conventions *see data dictionary*
### Exploration 
#### visualizations
#### bivariate statistical analysis
#### see below for more information
### Feature Engineering
#### dummies created 
#### RFE used to take out bottom 7 features of importance
### Modeling
#### see below

## Exploration
### Eploration was guided by four initial questions
  ####  -Does square footage influence value?
  ####  -Is the tax value dependent on the number of bathrooms?
  ####  -Is Tax value dependent on FIPS?
  ####  -Is Tax value dependent on the number of bedrooms?
### T-Test and SpearmanR were used for bivariate analysis

## Preparation
### *See prepare.py and acquire.py for information on disposition of data during SQL query and steps taken to prepare data for both exploration and model fitting


## Modeling
### Following models were used for Validation
#### Polynomial Regression
#### Tweedie Regressor
#### Lasso Lars 
### Tweedie Regressor was selected as the best because it had the smallest RMSE delta

## Data Dicitonary 

|  Feature     |  Description |
| -------------| ------------ |
| tax_value | approximate, taxable value of property; continuous; TARGET VALUE |
| bedroom      |  number of bedrooms; continuous|
| bathroom     |  number of bathrooms; continuous  |
| sqrft | floor space of property in sqare feet; coninuous|
| year_built | year that property was built; discrete |
| fips | second set of numbers in zip code; discrete |
| sqft_bin | square feet of homes split into groups for visualization |
