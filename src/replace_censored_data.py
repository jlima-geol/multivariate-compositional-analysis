def replace_censored(df, elements):
    df_clean = df.copy()
    for col in elements:
        non_zero = df_clean[col][df_clean[col] > 0]
        dl = non_zero.min() / 3
        df_clean[col] = df_clean[col].replace(0, dl)
        df_clean[col] = df_clean[col].fillna(dl)
    return df_clean