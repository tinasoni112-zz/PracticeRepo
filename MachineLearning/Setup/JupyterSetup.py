def setup():
    import pandas as pd
    import numpy as np

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    pd.set_option('display.width', 320)
    np.set_printoptions(linewidth=320)


# Read current path
def get_current_path():
    import os
    return os.getcwd()

