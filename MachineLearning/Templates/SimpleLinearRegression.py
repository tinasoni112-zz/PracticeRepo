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
filePath = r'SampleData\Simple_Linear_Regression_Data.csv'
data = read_CSV(filePath)

# Define Target Variable
target = 'Salary'

# Divide into X and y
X,y = divide_X_and_y(data=data, target=target)

# split the data into train and test
X_train, X_test, y_train, y_test = sklearn_train_test_split(X,y,test_size=1/3)

# Fitting linear regression on training set and predict on test set
model, y_predict = simple_linear_regression_sklearn(X_train, y_train, X_test)

# Visualise the training set results
plot_actual_vs_predict(X_train, y_train, model.predict(X_train))

# Visualise the test set results
plot_actual_vs_predict(X_test, y_test, y_predict)





