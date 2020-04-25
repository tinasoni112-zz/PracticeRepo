def linear_regression_sklearn(X_actual, y_actual):
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression().fit(X_actual, y_actual)
    return regressor

def regressor_prediction(regressor, X_actual):
    y_predict = regressor.predict(X_actual)
    return y_predict

def random_forest_regressor_sklearn(X_actual, y_actual,n_estimators = 100, random_state = 0):
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
    regressor.fit(X_actual,y_actual.iloc[:,0])
    return regressor


def XGB_regressor(X_actual, y_actual, n_estimators = 500, learning_rate=0.05, n_jobs=4):
    from xgboost import XGBRegressor
    regressor = XGBRegressor()
    regressor.fit(X_actual,y_actual)
    return regressor