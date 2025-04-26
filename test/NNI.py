import pandas as pd
import numpy as np
from scipy.spatial import KDTree


file_path = "/Users/scottliu/Desktop/easy_step_test/fixations.csv"
df = pd.read_csv(file_path)
if "fixation x [px]" in df.columns and "fixation y [px]" in df.columns:
    points = df[["fixation x [px]", "fixation y [px]"]].values
    tree = KDTree(points)
    distances, _ = tree.query(points, k=2)  # k=2 to exclude self-distance
    mean_d_o = np.mean(distances[:, 1])  # Exclude the first column (self-distance)
    n = len(points)
    area = (df["fixation x [px]"].max() - df["fixation x [px]"].min()) * (df["fixation y [px]"].max() - df["fixation y [px]"].min())
    mean_d_e = 1 / (2 * np.sqrt(n / area))
    NNI = mean_d_o / mean_d_e
    print("easy_Nearest Neighbor Index (NNI):", NNI)
else:
    print("Error: The dataset must contain 'x' and 'y' columns.")



file_path = "/Users/scottliu/Desktop/medium_step_test/fixations.csv"
df = pd.read_csv(file_path)
if "fixation x [px]" in df.columns and "fixation y [px]" in df.columns:
    points = df[["fixation x [px]", "fixation y [px]"]].values
    tree = KDTree(points)
    distances, _ = tree.query(points, k=2)  # k=2 to exclude self-distance
    mean_d_o = np.mean(distances[:, 1])  # Exclude the first column (self-distance)
    n = len(points)
    area = (df["fixation x [px]"].max() - df["fixation x [px]"].min()) * (df["fixation y [px]"].max() - df["fixation y [px]"].min())
    mean_d_e = 1 / (2 * np.sqrt(n / area))
    NNI = mean_d_o / mean_d_e
    print("medium_Nearest Neighbor Index (NNI):", NNI)
else:
    print("Error: The dataset must contain 'x' and 'y' columns.")



file_path = "/Users/scottliu/Desktop/hard_step_test/fixations.csv"
df = pd.read_csv(file_path)
if "fixation x [px]" in df.columns and "fixation y [px]" in df.columns:
    points = df[["fixation x [px]", "fixation y [px]"]].values
    tree = KDTree(points)
    distances, _ = tree.query(points, k=2)  # k=2 to exclude self-distance
    mean_d_o = np.mean(distances[:, 1])  # Exclude the first column (self-distance)
    n = len(points)
    area = (df["fixation x [px]"].max() - df["fixation x [px]"].min()) * (df["fixation y [px]"].max() - df["fixation y [px]"].min())
    mean_d_e = 1 / (2 * np.sqrt(n / area))
    NNI = mean_d_o / mean_d_e
    print("hard_Nearest Neighbor Index (NNI):", NNI)
else:
    print("Error: The dataset must contain 'x' and 'y' columns.")