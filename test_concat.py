import pandas as pd



output_file = "/Users/scottliu/Desktop/N1_P1/gaze.csv"


df = pd.read_csv(output_file)
start_timestamp = df["timestamp [ns]"].iloc[0]



t = (df["timestamp [ns]"] - start_timestamp) / 60000000000

print(type(t))

print("Modified file saved to:", t)


is_strictly_increasing = (t.diff().dropna() > 0).all()
print("Is strictly increasing:", is_strictly_increasing)
