import pandas as pd


file_path = "/Users/scottliu/Desktop/easy_step_test/saccades.csv"
df = pd.read_csv(file_path)
easy_fix = df["saccade id"].iloc[-1] - df["saccade id"].iloc[0]
print("Easy_ number of saccades:", easy_fix)


file_path = "/Users/scottliu/Desktop/medium_step_test/saccades.csv"
df = pd.read_csv(file_path)
medium_fix = df["saccade id"].iloc[-1] - df["saccade id"].iloc[0]
print("Medium_ number of saccades:", medium_fix)


file_path = "/Users/scottliu/Desktop/hard_step_test/saccades.csv"
df = pd.read_csv(file_path)
hard_fix = df["saccade id"].iloc[-1] - df["saccade id"].iloc[0]
print("Hard_ number of saccades:", hard_fix)