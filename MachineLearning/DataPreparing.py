# imports
import sklearn as sk
from sklearn import datasets as ds
import pandas as pd

# setting to view whole data than partial data with dots
pd.set_option('display.max_rows', None)  # Set it None to display all rows in the dataframe
pd.set_option('display.max_columns', None)  # Set it to None to display all columns in the dataframe

# load prebuilt sklearn data set - https://scikit-learn.org/stable/datasets/index.html#real-world-datasets
data = ds.load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)  # convert data into
df['target'] = pd.Series(data.target)

# Data View Commands
df.head()  # To display the top 5 rows
df.tail()  # To display the bottom 5 rows
df.dtypes  # Checking the data type
df.shape  # Total number of rows and columns

# General actions
df = df.rename(columns={'LoanStatNew': 'name', 'Description': 'description'})

# Beautify and preview the data types of dataframe
df_dtypes = pd.DataFrame(df.dtypes,columns=['dtypes'])
df_dtypes = df_dtypes.reset_index()
df_dtypes['name'] = df_dtypes['index']
df_dtypes = df_dtypes[['name','dtypes']]
df_dtypes['first value'] = df.loc[0].values
df_dtypes

# Duplicate Data
df[df.duplicated()]  # Rows containing duplicate data
half_count = len(df) / 2
df = df.dropna(thresh=half_count,axis=1) # Drop any column with more than 50% missing values


