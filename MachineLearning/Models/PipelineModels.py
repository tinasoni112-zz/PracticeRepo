def randomforest_regressor_pipeline(preprocessor, X_actual, y_actual,n_estimators = 100, random_state = 0):
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.pipeline import Pipeline

    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)

    # Bundle preprocessing and modeling code in a pipeline
    model_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('model', model)
                                 ])
    # fit the model
    model_pipeline.fit(X_actual, y_actual.iloc[:,0])

    return model_pipeline