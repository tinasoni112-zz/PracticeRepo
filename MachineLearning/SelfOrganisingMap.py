# https://towardsdatascience.com/self-organizing-maps-ff5853a118d4

# load prebuilt sklearn data set - https://scikit-learn.org/stable/datasets/index.html#real-world-datasets
data = ds.load_boston()
df = pd.DataFrame(data.data, columns=data.feature_names)  # convert data into
df['target'] = pd.Series(data.target)