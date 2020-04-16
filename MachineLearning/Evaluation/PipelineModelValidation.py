def cross_val_score_sklearn(model_pipeline, X, y, scoring='neg_mean_absolute_error', n_cross_val = 5):
    from sklearn.model_selection import cross_val_score
    scores = -1 * cross_val_score(model_pipeline, X, y.iloc[:,0],
                                  cv=n_cross_val,
                                  scoring=scoring)
    return scores.mean()

