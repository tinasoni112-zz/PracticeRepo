def calculate_accuracy(model, X_test,y_test) :
    accuracy = model.score(X_test, y_test)
    return accuracy

def create_confusion_matrix(y_test, y_predict) :
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_predict)
    return cm

def calc_rmse(y_actual, y_predicted):
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    rmse = sqrt(mean_squared_error(y_actual, y_predicted))
    return rmse

def highest_pvalue_column(statsmodel, sign_level = 0.05):
    highest_p_value_col = None
    pvalues = statsmodel.pvalues
    highest_p_value = max(pvalues)
    if(highest_p_value > sign_level):
        highest_p_value_col = pvalues[pvalues == highest_p_value].index.values[0]
    return highest_p_value_col

