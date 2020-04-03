def linear_regression_OLS_statsmodel(X, y):
    import statsmodels.api as sm
    # Add constant variable so intercept will be consider in stats model
    X = X.assign(Intercept=1)
    # create model
    regressor_OLS = sm.OLS(y,X).fit()
    return regressor_OLS



