# check null values in dataframe
def check_null_values(data):
    return data.isnull().sum()

# check null values percentage in dataframe
def check_null_percentage(data):
    return data.isnull().sum()/len(data) * 100

# Get columns having null values
def fetch_null_columns(data):
    return data.columns[data.isnull().any()].tolist()

def drop_columns_null_values(data, cols):
    return data.dropna(subset=cols,  axis = 1)

def drop_rows_null_values(data, cols):
    return data.dropna(subset=cols,  axis = 0)

# fill missing values with mean column values
def fillna_using_mean(data):
    return data.fillna(data.mean())