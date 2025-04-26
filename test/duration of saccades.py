import pandas as pd


file_path = "/Users/scottliu/Desktop/easy_step_test/saccades.csv"
df = pd.read_csv(file_path)
total_duration = df["duration [ms]"].sum()
average_duration = df["duration [ms]"].mean()
print("easy_Total duration [ms]:", total_duration)
print("easy_Average duration [ms]:", average_duration)


file_path = "/Users/scottliu/Desktop/medium_step_test/saccades.csv"
df = pd.read_csv(file_path)
total_duration = df["duration [ms]"].sum()
average_duration = df["duration [ms]"].mean()
print("medium_Total duration [ms]:", total_duration)
print("medium_Average duration [ms]:", average_duration)


file_path = "/Users/scottliu/Desktop/hard_step_test/saccades.csv"
df = pd.read_csv(file_path)
total_duration = df["duration [ms]"].sum()
average_duration = df["duration [ms]"].mean()
print("hard_Total duration [ms]:", total_duration)
print("hard_Average duration [ms]:", average_duration)