import pandas as pd
import numpy as np

"""fixation point based"""
file_path = "/Users/scottliu/Desktop/2+3_aoi/easy_aoi.csv"
df = pd.read_csv(file_path)
aoi_counts = df["aoi name"].value_counts()
total_fixations = aoi_counts.sum()
aoi_probabilities = aoi_counts / total_fixations
gaze_entropy = -np.sum(aoi_probabilities * np.log2(aoi_probabilities))

print(f"easy_Gaze Entropy: {gaze_entropy:.4f}")

file_path = "/Users/scottliu/Desktop/2+3_aoi/medium_aoi.csv"
df = pd.read_csv(file_path)
aoi_counts = df["aoi name"].value_counts()
total_fixations = aoi_counts.sum()
aoi_probabilities = aoi_counts / total_fixations
gaze_entropy = -np.sum(aoi_probabilities * np.log2(aoi_probabilities))

print(f"medium_Gaze Entropy: {gaze_entropy:.4f}")

file_path = "/Users/scottliu/Desktop/2+3_aoi/hard_aoi.csv"
df = pd.read_csv(file_path)
aoi_counts = df["aoi name"].value_counts()
total_fixations = aoi_counts.sum()
aoi_probabilities = aoi_counts / total_fixations
gaze_entropy = -np.sum(aoi_probabilities * np.log2(aoi_probabilities))

print(f"hard_Gaze Entropy: {gaze_entropy:.4f}")




# What is the maximum gaze entropy with four AOIs?
# The maximum entropy occurs when fixations are **evenly distributed** across all AOIs.
#
# For **four AOIs**, the ideal probability distribution is:
# \[
# p_1 = p_2 = p_3 = p_4 = \frac{1}{4} = 0.25
# \]
#
# Applying Shannon entropy formula:
# \[
# H_{\max} = - \sum_{i=1}^{4} (0.25 \log_2 0.25)
# \]
# \[
# = - 4 \times (0.25 \times -2)
# \]
# \[
# = 2.0 \text{ bits}
# \]
#
# So, the **maximum gaze entropy with four AOIs is 2.0 bits**.





"""duration based"""


import pandas as pd
import numpy as np


file_path = "/Users/scottliu/Desktop/2+3_aoi/easy_aoi.csv"
df = pd.read_csv(file_path)
aoi_list = ["Guide", "OR", "Progbars", "Combined total screen"]
df_filtered = df[df["aoi name"].isin(aoi_list)]
aoi_durations = df_filtered.groupby("aoi name")["fixation duration [ms]"].sum()
total_duration = aoi_durations.sum()
p_i = aoi_durations / total_duration
gaze_entropy = -np.sum(p_i * np.log2(p_i))

print(f"easy_Gaze Entropy (Fixation Duration-Based): {gaze_entropy:.4f} ")

file_path = "/Users/scottliu/Desktop/2+3_aoi/medium_aoi.csv"
df = pd.read_csv(file_path)
aoi_list = ["Guide", "OR", "Progbars", "Combined total screen"]
df_filtered = df[df["aoi name"].isin(aoi_list)]
aoi_durations = df_filtered.groupby("aoi name")["fixation duration [ms]"].sum()
total_duration = aoi_durations.sum()
p_i = aoi_durations / total_duration
gaze_entropy = -np.sum(p_i * np.log2(p_i))

print(f"medium_easy_Gaze Entropy (Fixation Duration-Based): {gaze_entropy:.4f} ")

file_path = "/Users/scottliu/Desktop/2+3_aoi/hard_aoi.csv"
df = pd.read_csv(file_path)
aoi_list = ["Guide", "OR", "Progbars", "Combined total screen"]
df_filtered = df[df["aoi name"].isin(aoi_list)]
aoi_durations = df_filtered.groupby("aoi name")["fixation duration [ms]"].sum()
total_duration = aoi_durations.sum()
p_i = aoi_durations / total_duration
gaze_entropy = -np.sum(p_i * np.log2(p_i))

print(f"hard_easy_Gaze Entropy (Fixation Duration-Based): {gaze_entropy:.4f} ")