# imports
from PracticeRepo.MachineLearning.EDA.BasicEDA import *
from PracticeRepo.MachineLearning.EDA.BasicEDA import create_dataframe
from PracticeRepo.MachineLearning.EDA.sklearnEDA import *
from PracticeRepo.MachineLearning.Models.RegressionModels import *
from PracticeRepo.MachineLearning.Evaluation.ModelValidation import *


# Step to reload the module
import PracticeRepo.MachineLearning.Evaluation.ModelValidation as mymodule
import PracticeRepo.MachineLearning.EDA.sklearnEDA as mymodule
import PracticeRepo.MachineLearning.Models.RegressionModels as mymodule
import importlib
importlib.reload(mymodule)

filepath = r'C:\Users\sonitina\PycharmProjects\Kaggle\PracticeRepo\MachineLearning\Templates\SampleData'
# Read test and train data
train_data = read_CSV(filepath+'\HousingPrice_train.csv',index_col='Id')
test_data = read_CSV(filepath+'\HousingPrice_test.csv',index_col='Id')

# Define Target Column
target = 'SalePrice'

# Remove rows having missing target values
train_data = drop_rows_null_values(train_data,[target])

# Divide it into X and Y
X_train_full, y_train_full = divide_X_and_y(train_data, target)

'''
# Handle missing values
'''
# Refer only numeric columns
X_train_num = get_numeric_data(X_train_full)

# print columns with missing values
missing_cols = fetch_null_columns(X_train_num)
print(missing_cols)

# Method - 1 : drop missing cols
X_train_dropna = drop_columns(X_train_num,missing_cols)

# split into train and validation
X_train, X_valid, y_train, y_valid = sklearn_train_test_split(X_train_dropna, y_train_full)

# Apply regression on this
regressor = random_forest_regressor_sklearn(X_train, y_train)

# calculate MAE
print(calc_mae(y_valid, regressor_prediction(regressor,X_valid)))

# split into train and validation
X_train, X_valid, y_train, y_valid = sklearn_train_test_split(X_train_num, y_train_full)

# Method - 2 : Apply Simple Imputer
X_train_imputer, imputer = sklearn_imputer(X_train)
X_valid_imputer = create_dataframe(imputer.transform(X_valid),X_valid.columns)
X_valid_imputer.index = X_valid.index

# Apply regression on this
regressor = random_forest_regressor_sklearn(X_train_imputer, y_train)

# calculate MAE
print(calc_mae(y_valid, regressor_prediction(regressor,X_valid_imputer)))
# 18630.30071917808

'''
# Handle Categorical values
'''
# List categorical columns
cat_columns = fetch_cat_columns(X_train_full)
print(cat_columns)

# Handle missing numeric data using imputer
X_train_full_impute = concat_df(sklearn_imputer(X_train_num)[0], sklearn_imputer(X_train_full[cat_columns],strategy='most_frequent')[0])

# Method 1 - Drop Categorical Variables
X_train_dropcat = drop_columns(X_train_full_impute, cat_columns)

# split into train and validation
X_train, X_valid, y_train, y_valid = sklearn_train_test_split(X_train_dropcat, y_train_full)

# Apply regression on this
regressor = random_forest_regressor_sklearn(X_train, y_train)

# calculate MAE
print(calc_mae(y_valid, regressor_prediction(regressor,X_valid)))
# 19576.93644977169

# Method 2- Label Encoding
X_train, X_valid, y_train, y_valid = sklearn_train_test_split(X_train_full_impute, y_train_full)

# Handle unknown categories in test/valid data when compare to train data
# Columns that can be safely label encoded
good_label_cols = get_good_label_cols(X_train,X_valid,cat_columns)
# Problematic columns that will be dropped from the dataset
bad_label_cols = subtract_cols(cat_columns, good_label_cols)

print('Categorical columns that will be label encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)

# Drop categorical columns that will not be encoded
X_train_label = drop_columns(X_train, bad_label_cols)
X_valid_label = drop_columns(X_valid, bad_label_cols)

# Apply label encoder
for col in good_label_cols:
    X_train_label, encoder = sklearn_label_encoding(X_train_label, col)
    X_valid_label[col] = encoder.transform(X_valid_label[col])

# Apply regression on this
regressor = random_forest_regressor_sklearn(X_train_label, y_train)

# calculate MAE
print(calc_mae(y_valid, regressor_prediction(regressor,X_valid_label)))
# 17816.84595890411

# Method 3 - One-hot encoding
X_train, X_valid, y_train, y_valid = sklearn_train_test_split(X_train_full_impute, y_train_full)

# Investigating cardinality
# Get number of unique entries in each column with categorical data
dict_unique_cat = create_unique_value_dict(X_train, cat_columns)
print(dict_unique_cat)

# Columns that will be one-hot encoded
low_cardinality_cols = fetch_low_cardinality_cols(X_train, cat_columns)

# Columns that will be dropped from the dataset
high_cardinality_cols = subtract_cols(cat_columns, low_cardinality_cols)

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)

# drop high cardinality cols
X_train_drop_highcard = drop_columns(X_train, high_cardinality_cols)
X_valid_drop_highcard = drop_columns(X_valid, high_cardinality_cols)

# Apply one-hot encoder to each column with categorical data
X_train_oh, oh_encoder = sklearn_one_hot_encode(X_train_drop_highcard, low_cardinality_cols)
X_valid_oh = create_dataframe(oh_encoder.transform(X_valid[low_cardinality_cols]),None)
X_valid_oh.index = X_valid.index

# Add one-hot encoded columns to numerical features
X_train_final_oh = concat_df(X_train_oh, X_train_drop_highcard[fetch_numeric_columns(X_train_drop_highcard)])
X_valid_final_oh = concat_df(X_valid_oh, X_valid_drop_highcard[fetch_numeric_columns(X_valid_drop_highcard)])

# Apply regression on this
regressor = random_forest_regressor_sklearn(X_train_final_oh, y_train)

# calculate MAE
print(calc_mae(y_valid, regressor_prediction(regressor,X_valid_final_oh)))
# 16506.65732876712

# Using XGBRegressor
xgb_regressor = XGB_regressor(X_train_final_oh, y_train)
print(calc_mae(y_valid, regressor_prediction(xgb_regressor,X_valid_final_oh)))


