import pandas as pd
from sklearn.decomposition import PCA

def run_pca(df, n_components=4):
    pca = PCA(n_components=n_components)
    scores = pca.fit_transform(df)
    loadings = pd.DataFrame(pca.components_.T, 
                            columns=[f"PC{i+1}" for i in range(n_components)],
                            index=df.columns)
    return pca, scores, loadings