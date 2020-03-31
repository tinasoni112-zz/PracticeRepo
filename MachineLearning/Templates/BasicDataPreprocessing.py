# Imports libraries/utilities
from PracticeRepo.MachineLearning.EDA.BasicEDA import *
from PracticeRepo.MachineLearning.EDA.sklearnEDA import *

# Import Datasets
filePath = r'C:\Users\sonitina\PycharmProjects\Kaggle\PracticeRepo\MachineLearning\Templates\SampleData\Preprocessing_Data.csv'
data = read_CSV(filePath)

# Define Target Variable
target = 'Purchased'

# Divide into X and y
X,y = divide_X_and_y(data=data, target=target)

# Handle missing data by fill them with Mean using Imputer
missing_cols = fetch_null_columns(X)
print(missing_cols)
X = fillna_using_mean(X)

# Handle categorical data
category_cols = fetch_cat_columns(X)
print(category_cols)

# Create dummy variables as its nominal category
dummy_variables_df = dummy_variables_pd(X,category_cols)

# Drop existing column and add these dummies to X
X = drop_columns(X,category_cols)
X = concat_df(X,dummy_variables_df)

# Convert labels as integer in target column
y[target] = label_encoding(y,target)

# split the data into train and test
X_train, X_test, y_train, y_test = sklearn_train_test_split(X,y)

# Feature Scaling
X_train = create_dataframe(scaler_sklearn(X_train),X_train.columns.values)
X_test = create_dataframe(scaler_sklearn(X_test),X_test.columns.values)
