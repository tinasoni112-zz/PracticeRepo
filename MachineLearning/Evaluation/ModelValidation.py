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
