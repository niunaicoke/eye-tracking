import pandas as pd


input_file = "/Users/scottliu/Desktop/Protocol_4_MARKER-MAPPER_Emma_1,_first_video_csv/gaze.csv"
output_file = "/Users/scottliu/Desktop/1+2_aoi/medium_gaze.csv"


df = pd.read_csv(input_file)
start_timestamp = df.iloc[0]['timestamp [ns]']
start_offset_ns = (36 * 60 + 40) * 1e9
end_offset_ns = (39 * 60 + 40) * 1e9
start_time_ns = start_timestamp + start_offset_ns
end_time_ns = start_timestamp + end_offset_ns
filtered_df = df[(df['timestamp [ns]'] >= start_time_ns) & (df['timestamp [ns]'] <= end_time_ns)]
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")



