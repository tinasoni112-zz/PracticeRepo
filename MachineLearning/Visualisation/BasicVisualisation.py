def plot_corr(corr_matrix,size=10):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr_matrix)
    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

# print histogram
def plot_freq_histogram(data, figsize=None, title = None):
    import matplotlib.pyplot as plt
    plt.hist(data,figsize=figsize)
    plt.title(title)

def plot_actual_vs_predict(x_actual , y_actual , y_predict):
    import matplotlib.pyplot as plt
    plt.scatter(x_actual, y_actual, color = 'red')
    plt.plot(x_actual, y_predict, color = 'blue')
    plt.xlabel(x_actual.columns.values[0])
    plt.ylabel(y_actual.columns.values[0])

def plot_line_graph(X, Y):
    import matplotlib.pyplot as plt
    plt.plot(X,Y)


