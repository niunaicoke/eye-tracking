import pandas as pd

# File paths
input_file = "/Users/scottliu/Desktop/Timeseries Data, EK1, First part video, 58mins 01secs/2024-09-26_13-40-52-91692b0f/saccades.csv"
output_file = "/Users/scottliu/Desktop/medium_step_test/saccades.csv"

df = pd.read_csv(input_file)
start_timestamp = df["start timestamp [ns]"].iloc[0]
start_offset_ns = (35 * 60 + 40) * 1e9
end_offset_ns = (40 * 60 + 40) * 1e9
start_ns = start_timestamp + start_offset_ns
end_ns = start_timestamp + end_offset_ns
filtered_df = df[(df["start timestamp [ns]"] >= start_ns) & (df["start timestamp [ns]"] <= end_ns)]
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
