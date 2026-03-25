import pandas as pd
from sklearn.decomposition import PCA

def run_pca(df, n_components=4):
    """Run PCA and return pca object, scores (DataFrame) and loadings (DataFrame)."""
    
    pca = PCA(n_components=n_components)
    scores_arr = pca.fit_transform(df)

    # Preserva índice e nomeia PCs
    scores = pd.DataFrame(
        scores_arr,
        index=df.index,
        columns=[f"PC{i+1}" for i in range(n_components)]
    )

    # Loadings já estava ótimo, só deixei explícito
    loadings = pd.DataFrame(
        pca.components_.T,
        index=df.columns,
        columns=[f"PC{i+1}" for i in range(n_components)]
    )

    return pca, scores, loadings
