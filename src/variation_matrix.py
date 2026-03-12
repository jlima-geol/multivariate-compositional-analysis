import numpy as np
import pandas as pd

def variation_matrix(df):
    """Compute Aitchison variation matrix."""
    cols = df.columns
    V = pd.DataFrame(index=cols, columns=cols, dtype=float)

    for i in cols:
        for j in cols:
            V.loc[i, j] = np.var(np.log(df[i] / df[j]))

    return V