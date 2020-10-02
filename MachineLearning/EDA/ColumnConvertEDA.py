def convert_col_to_date(data,col,format):
    import pandas as pd
    data[col] = pd.to_datetime(data[col], format=format,errors='coerce')

def convert_col_to_category(data, *cols):
    for col in cols:
        data[col] = data[col].astype('category')