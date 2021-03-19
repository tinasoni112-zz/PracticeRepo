def divide_X_and_y(data, target):
    X = data.loc[:, data.columns != target]
    y = data.loc[:, data.columns == target]
    return X,y

def split_date_column(data, datecol):
    data[datecol+'_Day'] = data[datecol].dt.day
    data[datecol+'_Month'] = data[datecol].dt.month
    data[datecol+'_Year'] = data[datecol].dt.year
    data[datecol+'_Quarter'] = data[datecol].dt.quarter


def split_time_column(data, datecol):
    data[datecol+'_Hour'] = data[datecol].dt.hour
    data[datecol+'_Minute'] = data[datecol].dt.minute
    data[datecol+'_Second'] = data[datecol].dt.second


def divide_train_valid_test_data(data, valid_fraction=0.1):
    valid_size = int(len(data) * valid_fraction)
    train = data[:-2 * valid_size]
    valid = data[-2*valid_size : -valid_size]
    test = data[-valid_size:]
    return train, valid, test
