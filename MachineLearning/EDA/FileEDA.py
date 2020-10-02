# Read CSV file
def read_CSV(filepath, index_col = None, date_cols = None, names = None ):
    import pandas as pd
    data = pd.read_csv(filepath, index_col=index_col, parse_dates = date_cols, names=names)
    return data

# Read Excel file
def read_Excel(filepath, index_col = None ):
    import pandas as pd
    data = pd.read_excel(filepath, index_col = index_col)
    return data

