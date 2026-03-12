import numpy as np
import pandas as pd

def clr(df):
    """Centered log-ratio transformation."""
    gm = df.apply(lambda x: np.exp(np.log(x).mean()), axis=1)
    return np.log(df.div(gm, axis=0))

def alr(df, denominator):
    """Additive log-ratio transformation."""
    return np.log(df.div(df[denominator], axis=0))