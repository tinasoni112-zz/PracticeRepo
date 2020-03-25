def get_top_abs_correlations(corr_matrix, n=5):
    au_corr = corr_matrix.abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]


def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def corr_with_given_col(corr_matrix, col, thresh = 0.5):
    # Correlation with given variable
    print(corr_matrix[col])

    # top correlation
    print(corr_matrix[corr_matrix[col] > thresh][col])

def fetch_top_correlated_variables(corr_matrix, thresh = 0.5):
    corr_matrix_sorted = corr_matrix.abs().unstack().sort_values(ascending=False)
    return corr_matrix_sorted[corr_matrix_sorted > thresh]

