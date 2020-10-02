def setup() :
    import pandas as pd
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

# Read current path
def get_current_path():
    import os
    return os.getcwd()