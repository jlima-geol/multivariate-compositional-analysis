import numpy as np
import pandas as pd

def clr(df):
    """Centered log-ratio transformation."""
    gm = df.apply(lambda x: np.exp(np.log(x).mean()), axis=1)
    return pd.DataFrame(
        np.log(df.div(gm, axis=0)),
        columns=df.columns,
        index=df.index
    )

def alr(df, denominator):
    """Additive log-ratio transformation."""
    return pd.DataFrame(
        np.log(df.div(df[denominator], axis=0)),
        columns=df.columns,
        index=df.index
    )