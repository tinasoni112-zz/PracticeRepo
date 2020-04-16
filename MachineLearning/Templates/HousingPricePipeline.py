# imports
from PracticeRepo.MachineLearning.EDA.PipelineEDA import *
from PracticeRepo.MachineLearning.Models.PipelineModels import *
from PracticeRepo.MachineLearning.EDA.BasicEDA import *
from PracticeRepo.MachineLearning.EDA.sklearnEDA import *
from PracticeRepo.MachineLearning.Evaluation.ModelValidation import *
from PracticeRepo.MachineLearning.Evaluation.PipelineModelValidation import *
from PracticeRepo.MachineLearning.Visualisation.BasicVisualisation import *

filepath = r'C:\Users\sonitina\PycharmProjects\Kaggle\PracticeRepo\MachineLearning\Templates\SampleData'

# Read test and train data
train_data = read_CSV(filepath+'\HousingPrice_train.csv',index_col='Id')
test_data = read_CSV(filepath+'\HousingPrice_test.csv',index_col='Id')

# Define Target Column
target = 'SalePrice'

# Separate target from predictors
X,y = divide_X_and_y(train_data, target)

# Divide data into training and validation subsets
X_train_full, X_valid_full, y_train, y_valid = sklearn_train_test_split(X, y)

# Select categorical columns with relatively low cardinality (convenient but arbitrary)
cat_cols = fetch_low_cardinality_cols(X_train_full, fetch_cat_columns(X_train_full))
num_cols = fetch_numeric_columns(X_train_full)

full_cols = cat_cols + num_cols

# create subset of train and valid
X_train = X_train_full[full_cols]
X_valid = X_valid_full[full_cols]

# basic preprocessor pipeline
preprocessor = basic_preprocess_pipeline(num_cols, cat_cols)

# model pipeline
model = randomforest_regressor_pipeline(preprocessor, X_train, y_train)

# validation
y_predict = model.predict(X_valid)

# mae
mae = calc_mae(y_valid, y_predict)
print(mae)

# cross validation
n_estimator_list = list(range(50,450,50))
average_scores = [cross_val_score_sklearn(randomforest_regressor_pipeline(preprocessor, X_train, y_train, n_estimator), X_train, y_train) for n_estimator in n_estimator_list]
average_scores = [x.mean() for x in average_scores]
results = create_dict_from_list(n_estimator_list, average_scores)

# Check your answer
plot_line_graph(list(results.keys()),list(results.values()))