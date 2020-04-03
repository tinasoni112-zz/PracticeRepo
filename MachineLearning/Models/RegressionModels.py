def linear_regression_sklearn(X_train,y_train,X_test):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression().fit(X_train,y_train)
    y_predict = regressor.predict(X_test)
    return regressor, y_predict
