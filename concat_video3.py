import pandas as pd
import os

# Define paths
v1_path = "/home/yulab/Desktop/N5/N5_P1/Timeseries Data, Nov5, procedure1, vid1/2024-10-21_09-20-34-aa1e6db9"
v2_path = "/home/yulab/Desktop/N5/N5_P1/Timeseries Data, Nov5, procedure1, vid2/2024-10-21_10-18-06-e77cda98"
v3_path = "/home/yulab/Desktop/N5/N5_P1/Timeseries Data, Nov5, procedure1, vid3/2024-10-21_10-42-56-ceb1d2f2"
output_path = "/home/yulab/Desktop/N5/N5_P1"

# Ensure output directory exists
os.makedirs(output_path, exist_ok=True)

# Files to combine
files = ["gaze.csv", "saccades.csv", "fixations.csv"]

# Combine each file
for file in files:
    v1_df = pd.read_csv(os.path.join(v1_path, file))
    v2_df = pd.read_csv(os.path.join(v2_path, file))
    v3_df = pd.read_csv(os.path.join(v3_path, file))
    combined_df = pd.concat([v1_df, v2_df, v3_df], ignore_index=True)
    combined_df.to_csv(os.path.join(output_path, file), index=False)

print("Files successfully combined and saved to:", output_path)
