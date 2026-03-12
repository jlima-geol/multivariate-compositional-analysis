Multivariate Analysis of Compositional Data

A Data Analysis case study using synthetic geochemical data

This project demonstrates an end‑to‑end multivariate analysis workflow applied to compositional data, using a fully synthetic dataset modeled after real-world geochemical systems.
It reproduces the analytical pipeline I developed during my PhD research, but no proprietary or embargoed data is used.

Please note that data intrepretation is not included here. For the interpretation of a real-worl geochemical dataset, refer to Chapter 6 - Multivariate Analysis of the thesis:

  Lima Torres, J. L. (2025). Multiple mineralization and fluid flow phases in the Central African Copperbelt – Implications for the age dating of the ore-forming processes.

The PhD thesis can be found at https://lnkd.in/dSdsMdE4

- Project Goals

    This repository showcases how to:

    - Handle censored values and detection limits
    - Apply log-ratio transformations (clr, alr)
    - Compute and visualize a variation matrix
    - Perform PCA on compositional data
    - Identify natural groups using DBSCAN
    - Test group separation using PERMANOVA
    - Communicate insights clearly through notebooks and visualizations

- Tech Stack
    - Python
    - pandas, numpy
    - scikit-learn (PCA, DBSCAN)
    - scikit-bio (PERMANOVA)
    - seaborn, matplotlib
    - jupyter notebooks

- Repository Structure

    notebooks/      → step-by-step analysis  
    src/            → reusable functions  
    data/           → synthetic raw + processed data  

- Synthetic Dataset

    The dataset simulates:

    - High-variance element pairs (e.g., SO₄–Ca, Mn–Mg)
    - Low-variance pairs (e.g., Br–F, F–Mn)
    - Two natural clusters detectable by DBSCAN
    - PCA structure similar to real geochemical systems
    - Log-ratio behavior consistent with compositional constraints

- How to Run

    pip install -r requirements.txt
    jupyter lab

- License

    MIT License — free to use, modify, and share.


--> Project Status

    This project is currently under active development.
