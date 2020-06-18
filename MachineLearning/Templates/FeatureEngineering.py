# Imports libraries/utilities
from PracticeRepo.MachineLearning.EDA.BasicEDA import *
from PracticeRepo.MachineLearning.EDA.sklearnEDA import *
from PracticeRepo.MachineLearning.EDA.CategoricalEDA import *
from PracticeRepo.MachineLearning.Models.ClassificationModels import *
from PracticeRepo.MachineLearning.Evaluation.ModelValidation import *

# Step to reload the module
import PracticeRepo.MachineLearning.EDA.BasicEDA as mymodule
import importlib
importlib.reload(mymodule)

# define variables
date_cols=['click_time']
cat_cols = ['ip', 'app', 'device', 'os', 'channel']
target = 'is_attributed'

# Import Datasets
filePath = r'C:\Users\sonitina\PycharmProjects\Kaggle\PracticeRepo\MachineLearning\Templates\SampleData\Feature_Engineering_Data.csv'
data = read_CSV(filePath, date_cols=date_cols)

# view summary
data_summary = basic_data_summary(data)
check_null_percentage(data)

data['ip'].describe()

# Handle missing data - drop it as its one column with 80 percent null values
null_columns = fetch_null_columns(data)
data =  drop_columns(data, null_columns)

# Add new columns for timestamp features day, hour, minute, and second and drop date column
for date in date_cols:
    split_time_column(data, date)
    # data = drop_columns(data, date)

# Handle categorical columns - default way is labelencoding
for cat in cat_cols:
    encoded_data,_ = sklearn_label_encoding(data, cat)
    data[cat] = encoded_data[cat]

# add interactions features
interaction_features_df = create_interaction_features(data, cat_cols)
data = join_dataframe(data, interaction_features_df)

for cat in interaction_features_df.columns:
    encoded_data,_ = sklearn_label_encoding(data, cat)
    data[cat] = encoded_data[cat]

# Generating numerical features - Number of events in the past - say 6 hours
timeline = '6h'
data["past_events_in_"+timeline] = count_past_events(data[date_cols[0]], timeline)

test_groupby = data.groupby(date_cols[0])['ip']
data['ip'].summary()


# split into train,valid and test data
train, valid, test = divide_train_valid_test_data(data)

# apply model
y_predict, gbm_model = lightgbm_model(train, valid, test, target, num_round=100)

# validate model
score = calc_roc_auc_score(test[target], y_predict)
print(score)

