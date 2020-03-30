def plot_heatmap(corr_matrix, size = 20):
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, ax = plt.subplots(figsize=(size, size))
    sns.heatmap(corr_matrix, annot=True,ax=ax)

def plot_pairplot(data):
    import seaborn as sns
    sns.set(style="ticks", color_codes=True)
    sns.pairplot(data)

def plot_scatterplot(x,y,data, label=None, figsize = (10,10)):
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.scatterplot(x,y, data = data, hue=label)
    plt.title(x+' vs '+y)
    plt.figure(figsize = figsize)

def plot_histogram(data, figsize=(10, 10)):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure(figsize=figsize)
    sns.distplot(data)