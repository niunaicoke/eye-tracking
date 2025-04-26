import pandas as pd


input_file = "/Users/scottliu/Desktop/Timeseries Data, EK1, First part video, 58mins 01secs/2024-09-26_13-40-52-91692b0f/fixations.csv"
output_file = "/Users/scottliu/Desktop/easy_step_test/fixations.csv"


df = pd.read_csv(input_file)
start_timestamp = df["start timestamp [ns]"].iloc[0]
start_offset_ns = (6 * 60 + 45) * 1e9
end_offset_ns = (11 * 60 + 45) * 1e9
start_ns = start_timestamp + start_offset_ns
end_ns = start_timestamp + end_offset_ns
filtered_df = df[(df["start timestamp [ns]"] >= start_ns) & (df["start timestamp [ns]"] <= end_ns)]
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
