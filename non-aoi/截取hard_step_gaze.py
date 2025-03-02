import pandas as pd


input_file = "/Users/scottliu/Desktop/Timeseries Data, EK1, Second part video, 30mins 05secs/2024-09-26_14-39-05-0f5c64c1/gaze.csv"
output_file = "/Users/scottliu/Desktop/hard_step_test/gaze.csv"

df = pd.read_csv(input_file)
start_timestamp = df.iloc[0]['timestamp [ns]']
start_offset_ns = (25 * 60 ) * 1e9
end_offset_ns = (30 * 60 ) * 1e9
start_time_ns = start_timestamp + start_offset_ns
end_time_ns = start_timestamp + end_offset_ns
filtered_df = df[(df['timestamp [ns]'] >= start_time_ns) & (df['timestamp [ns]'] <= end_time_ns)]
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
