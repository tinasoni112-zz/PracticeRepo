# Import libraries/utilities
from PracticeRepo.MachineLearning.EDA.BasicEDA import *
from PracticeRepo.MachineLearning.EDA.sklearnEDA import *
from PracticeRepo.MachineLearning.Models.RegressionModels import *
from PracticeRepo.MachineLearning.Visualisation.BasicVisualisation import *
from PracticeRepo.MachineLearning.Models.StatsModels import *
from PracticeRepo.MachineLearning.Evaluation.ModelValidation import *

# Step to reload the module
import PracticeRepo.MachineLearning.Evaluation.ModelValidation as mymodule
import importlib
importlib.reload(mymodule)

# PreProcess data
# Import Datasets
filePath = r'SampleData\MultipleLinearRegression.csv'
data = read_CSV(filePath)

# Define Target Variable
target = 'Profit'

# Divide into X and y
X,y = divide_X_and_y(data=data, target=target)

# Handle categorical data
category_cols = fetch_cat_columns(X)
print(category_cols)

# Create dummy variables as its nominal category
dummy_variables_df = dummy_variables_pd(X,category_cols)

# Drop existing column and add these dummies to X
X = drop_columns(X,category_cols)
X = concat_df(X,dummy_variables_df)

# split the data into train and test
X_train, X_test, y_train, y_test = sklearn_train_test_split(X,y)

# Fitting  linear regression on training set and predict on test set
model, y_predict = linear_regression_sklearn(X_train, y_train, X_test)

# Build the optimal model using Backward elimination
# Model with all predictors
regressor_OLS = linear_regression_OLS_statsmodel(X, y)
# View summary
regressor_OLS.summary()

# Now remove predictor having higher p-value
while True:
    highest_p_value_col = highest_pvalue_column(regressor_OLS)
    print('highest_p_value_col',highest_p_value_col)
    if highest_p_value_col is None:
        break
    else:
        X = drop_columns(X, highest_p_value_col)
        regressor_OLS = linear_regression_OLS_statsmodel(X,y)

# View Final summary
regressor_OLS.summary()

