def apply_exp(data):
    import numpy as np
    return np.exp(data)

def apply_log(data, col):
    import numpy as np
    return np.log(data[col]+1)

