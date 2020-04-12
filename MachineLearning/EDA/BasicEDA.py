# Read Excel file
def read_Excel(filepath, index_col = None ):
    import pandas as pd
    data = pd.read_excel(filepath, index_col = index_col)
    return data

# Read CSV file
def read_CSV(filepath, index_col = None ):
    import pandas as pd
    data = pd.read_csv(filepath, index_col=index_col)
    return data

# Read current path
def get_current_path():
    import os
    return os.getcwd()

# print summary info of data
def basic_data_summary(data):
    print(data.info())
    desribe_data = data.describe(include = "all")
    return desribe_data

def divide_X_and_y(data, target):
    X = data.loc[:, data.columns != target]
    y = data.loc[:, data.columns == target]
    return X,y

# list numeric columns
def list_numeric_cols(data):
    import numpy as np
    numeric_cols = data.select_dtypes([np.number]).columns.values
    return numeric_cols

def convert_col_to_date(data,col,format):
    import pandas as pd
    data[col] = pd.to_datetime(data[col], format=format,errors='coerce')

def convert_col_to_category(data, *cols):
    for col in cols:
        data[col] = data[col].astype('category')

# filter dataframe on column names regex
def filter_dataframe(data, col_regex):
    return data.filter(regex = col_regex)

# Update column names of dataframe by removing given regex string
def update_column_names(data, col_regex):
    data.columns = data.columns.str.replace(col_regex,'')

# check null values in dataframe
def check_null_values(data):
    return data.isnull().sum()

# check null values percentage in dataframe
def check_null_percentage(data):
    return data.isnull().sum()/len(data) * 100

def sort_values_df(data):
    data.sort_values(inplace=True)

def linear_model_summary(X,y):
    import statsmodels.api as sm
    model = sm.OLS(y,X).fit()
    return model.summary()

def drop_columns_null_values(data, cols):
    return data.dropna(subset=cols,  axis = 1)

def drop_rows_null_values(data, cols):
    return data.dropna(subset=cols,  axis = 0)

# Get columns having null values
def fetch_null_columns(data):
    return data.columns[data.isnull().any()].tolist()

def drop_columns(data, col):
    return data.drop(col, axis = 1)

def split_date_column(data, datecol):
    data[datecol+'_Day'] = data[datecol].dt.day
    data[datecol+'_Month'] = data[datecol].dt.month
    data[datecol+'_Year'] = data[datecol].dt.year
    data[datecol+'_Quarter'] = data[datecol].dt.quarter



def dummy_variables_pd(data,col):
    import pandas as pd
    encoded_data = pd.get_dummies(data[col], prefix=col, drop_first=True)
    return encoded_data

def fetch_categories(data, col):
    return data[col].cat.categories.values

def flatten_list_of_list(list_of_list):
    flat_list =  [item for sublist in list_of_list for item in sublist]
    return flat_list

def concatenate_dataframes_by_col(*df) :
    import pandas as pd
    final_df = pd.concat(df, axis=1)
    return final_df

def flatmap_list_of_df(df) :
    import pandas as pd
    final_df = pd.concat(df)
    return final_df

def calc_corr_matrix(data):
    return data.corr()

def concat_df(X,y):
    import pandas as pd
    df = pd.concat([X, y], axis=1)
    return df

def concat_df_by_row(X,y):
    import pandas as pd
    df = pd.concat([X, y], axis=0)
    return df

def apply_log(data, col):
    import numpy as np
    return np.log(data[col]+1)

def get_numeric_data(data):
    import numpy as np
    return data.select_dtypes(include=np.number)


def get_object_data(data):
    import numpy as np
    return data.select_dtypes(include=np.object)

def create_empty_dataframe():
    import pandas as pd
    return pd.DataFrame()

def apply_exp(data):
    import numpy as np
    return np.exp(data)

def fetch_unique_values(data,col):
    return data[col].unique().tolist()

def fetch_data_by_index(data,index_list):
    return data[data.index.isin(index_list)]

def fetch_index_by_value(data,col, value):
    return data[data[col]== value].index

def create_dataframe_prefix_colname(array,colname):
    import pandas as pd
    colnames = [colname + str(i + 1) for i in range(array.shape[1])]
    return pd.DataFrame(data=array, columns=colnames)

def create_dataframe(array,colnames):
    import pandas as pd
    return pd.DataFrame(data=array, columns=colnames)

# fill missing values with mean column values
def fillna_using_mean(data):
    return data.fillna(data.mean())

# fetch columns of category type
def fetch_cat_columns(data):
    return  data.select_dtypes(include=['object','category']).columns.values.tolist()

# fetch columns of category type
def fetch_numeric_columns(data):
    return  data.select_dtypes(exclude=['object','category']).columns.values.tolist()

# Add constant column having values as one at starting of array
def add_constant_column_ones_array(data_array):
    import numpy as np
    data_array = np.append(arr =np.ones((50,1)).astype(int), values=data_array, axis=1)
    return data_array

def get_good_label_cols(X_train, X_test, cols):
    return [col for col in cols if set(X_train[col]) == set(X_test[col])]

def subtract_cols(full_cols, subset_cols):
    return list(set(full_cols) - set(subset_cols))

def create_unique_value_dict(data, cols):
    list_nunique = list(map(lambda col: data[col].nunique(), cols))
    dict_unique = dict(zip(cols, list_nunique))
    return sorted(dict_unique.items(), key=lambda x: x[1])

def fetch_low_cardinality_cols(data, cols, threshold = 10):
    return [col for col in cols if data[col].nunique() < threshold]