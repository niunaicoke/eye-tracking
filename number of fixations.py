import pandas as pd


file_path = "/Users/scottliu/Desktop/easy_step_test/fixations.csv"
df = pd.read_csv(file_path)
easy_fix = df["fixation id"].iloc[-1] - df["fixation id"].iloc[0]
print("Easy_ number of fixations:", easy_fix)


file_path = "/Users/scottliu/Desktop/medium_step_test/fixations.csv"
df = pd.read_csv(file_path)
medium_fix = df["fixation id"].iloc[-1] - df["fixation id"].iloc[0]
print("Medium_ number of fixations:", medium_fix)


file_path = "/Users/scottliu/Desktop/hard_step_test/fixations.csv"
df = pd.read_csv(file_path)
hard_fix = df["fixation id"].iloc[-1] - df["fixation id"].iloc[0]
print("Hard_ number of fixations:", hard_fix)