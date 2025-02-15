import pandas as pd


input_file = "/Users/scottliu/Desktop/Timeseries Data, EK1, First part video, 58mins 01secs/2024-09-26_13-40-52-91692b0f/gaze.csv"
output_file = "/Users/scottliu/Desktop/easy_step_test/filtered_gaze.csv"


df = pd.read_csv(input_file)
start_timestamp = df.iloc[0]['timestamp [ns]']
start_offset_ns = (7 * 60 + 45) * 1e9
end_offset_ns = (10 * 60 + 45) * 1e9
start_time_ns = start_timestamp + start_offset_ns
end_time_ns = start_timestamp + end_offset_ns
filtered_df = df[(df['timestamp [ns]'] >= start_time_ns) & (df['timestamp [ns]'] <= end_time_ns)]
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
