# Import libraries/utilities
from PracticeRepo.MachineLearning.EDA.BasicEDA import *
from PracticeRepo.MachineLearning.EDA.sklearnEDA import *
from PracticeRepo.MachineLearning.Models.RegressionModels import *
from PracticeRepo.MachineLearning.Visualisation.BasicVisualisation import *

# Step to reload the module
import PracticeRepo.MachineLearning.Models.RegressionModels as mymodule
import importlib
importlib.reload(mymodule)

# PreProcess data
# Import Datasets
filePath = r'C:\Users\sonitina\PycharmProjects\Kaggle\PracticeRepo\MachineLearning\Templates\SampleData\Polynomial_Regression_Data.csv'
data = read_CSV(filePath)

# Define Target Variable
target = 'Salary'

# Divide into X and y
X,y = divide_X_and_y(data=data, target=target)

# # split the data into train and test - small data set
# X_train, X_test, y_train, y_test = sklearn_train_test_split(X,y,test_size=1/3)

# Remove column Position as its category and equivalent numeric version present as level
cat_col = fetch_cat_columns(X)
X = drop_columns(X, cat_col)

# Create polynomial matrix for X
X_poly = sklearn_polynomial_features(X, n_degree=4)

# Fitting linear regression on polynomial matrix
model = linear_regression_sklearn(X_poly ,y)
y_predict = regressor_prediction(model, X_poly)

# Visualise it
plot_actual_vs_predict(X, y, y_predict)



