import numpy as np
import pandas as pd

def variation_matrix(df):
    """Compute Aitchison variation matrix (vectorized)."""
    cols = df.columns
    n = len(cols)
    V = np.zeros((n, n))
    arr = df.values
    for i in range(n):
        for j in range(n):
            V[i, j] = np.var(np.log(arr[:, i] / arr[:, j]))
    return pd.DataFrame(V, index=cols, columns=cols)