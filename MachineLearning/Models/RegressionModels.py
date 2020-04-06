def linear_regression_sklearn(X_actual, y_actual):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression().fit(X_actual, y_actual)
    return regressor

def regressor_prediction(regressor, X_actual):
    y_predict = regressor.predict(X_actual)
    return y_predict
