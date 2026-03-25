import numpy as np
import pandas as pd

np.random.seed(42)

## 1. Define element groups

halogens = ["Br", "Cl", "F", "SO4"]
carbonates = ["Ca", "Mg", "Sr"]
metals = ["Cu", "Co", "Pb", "Zn"]
alkalis = ["Li", "Na", "K"]
others = ["Mn", "Fe", "Ba"]

elements = halogens + carbonates + metals + alkalis + others

## 2. Create two clusters

n1, n2 = 300, 300

# Cluster A: halogen-rich, metal-poor
A = pd.DataFrame({
    "Br":  np.random.lognormal(mean=0.5, sigma=0.4, size=n1),
    "Cl":  np.random.lognormal(mean=0.6, sigma=0.4, size=n1),
    "F":   np.random.lognormal(mean=-1.0, sigma=0.3, size=n1),
    "SO4": np.random.lognormal(mean=0.8, sigma=0.5, size=n1),

    "Ca":  np.random.lognormal(mean=0.2, sigma=0.6, size=n1),
    "Mg":  np.random.lognormal(mean=0.1, sigma=0.6, size=n1),
    "Sr":  np.random.lognormal(mean=-0.2, sigma=0.5, size=n1),

    "Cu":  np.random.lognormal(mean=-1.2, sigma=0.4, size=n1),
    "Co":  np.random.lognormal(mean=-1.0, sigma=0.4, size=n1),
    "Pb":  np.random.lognormal(mean=-1.1, sigma=0.4, size=n1),
    "Zn":  np.random.lognormal(mean=-1.0, sigma=0.4, size=n1),

    "Li":  np.random.lognormal(mean=0.3, sigma=0.4, size=n1),
    "Na":  np.random.lognormal(mean=1.0, sigma=0.3, size=n1),
    "K":   np.random.lognormal(mean=0.2, sigma=0.3, size=n1),

    "Mn":  np.random.lognormal(mean=0.4, sigma=0.5, size=n1),
    "Fe":  np.random.lognormal(mean=0.3, sigma=0.5, size=n1),
    "Ba":  np.random.lognormal(mean=-0.3, sigma=0.4, size=n1),
})

# Cluster B: metal-rich, halogen-poor
B = pd.DataFrame({
    "Br":  np.random.lognormal(mean=-1.0, sigma=0.4, size=n2),
    "Cl":  np.random.lognormal(mean=-0.8, sigma=0.4, size=n2),
    "F":   np.random.lognormal(mean=-1.2, sigma=0.3, size=n2),
    "SO4": np.random.lognormal(mean=-0.5, sigma=0.5, size=n2),

    "Ca":  np.random.lognormal(mean=0.4, sigma=0.6, size=n2),
    "Mg":  np.random.lognormal(mean=0.5, sigma=0.6, size=n2),
    "Sr":  np.random.lognormal(mean=0.2, sigma=0.5, size=n2),

    "Cu":  np.random.lognormal(mean=0.8, sigma=0.4, size=n2),
    "Co":  np.random.lognormal(mean=0.7, sigma=0.4, size=n2),
    "Pb":  np.random.lognormal(mean=0.9, sigma=0.4, size=n2),
    "Zn":  np.random.lognormal(mean=0.8, sigma=0.4, size=n2),

    "Li":  np.random.lognormal(mean=-0.2, sigma=0.4, size=n2),
    "Na":  np.random.lognormal(mean=0.8, sigma=0.3, size=n2),
    "K":   np.random.lognormal(mean=0.1, sigma=0.3, size=n2),

    "Mn":  np.random.lognormal(mean=0.6, sigma=0.5, size=n2),
    "Fe":  np.random.lognormal(mean=0.7, sigma=0.5, size=n2),
    "Ba":  np.random.lognormal(mean=0.3, sigma=0.4, size=n2),
})

## 3. Combine clusters

df = pd.concat([A, B], ignore_index=True)
df["cluster_true"] = ["A"] * n1 + ["B"] * n2

## 4. Normalize to compositional data (closure)

df_comp = df.copy()
df_comp[elements] = df_comp[elements].div(df_comp[elements].sum(axis=1), axis=0)

## 5. Save

def main():
    df_comp.to_csv("data/raw/synthetic_geochemistry_raw.csv", index=False)
    print("Synthetic dataset saved to data/raw/")

if __name__ == "__main__":
    main()
