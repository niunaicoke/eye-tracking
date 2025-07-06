

import pandas as pd
from time_config import Time
T= Time()



def mean_fixations (minute=1, sec=1, label="x", data=""):
    t_before_task_in_seconds =120
    t_after_task_in_seconds=120
    start_timestamp = data.iloc[0]['start timestamp [ns]']+ (minute * 60 + sec) * 1e9
    pretask_ns = start_timestamp - t_before_task_in_seconds * 1e9
    posttask_ns = start_timestamp+ t_after_task_in_seconds * 1e9
    df = data[(data['start timestamp [ns]'] >= pretask_ns) & (data['end timestamp [ns]'] <= posttask_ns)]
    duration = pd.Series(df['duration [ms]'])
    duration = duration.sum()
    num_fixations = df["fixation id"].count()
    print(f"The mean fixations for {label} is {duration / num_fixations} ms per fixation")





for i in range(1, 10):
    # P1
    data = pd.read_csv(f"/Users/scottliu/Desktop/Peiran Processed Data/N{i}/N{i}_P1/fixations.csv")
    x = mean_fixations(getattr(T, f"N{i}_P1_e")[0], getattr(T, f"N{i}_P1_e")[1], f"N{i}_P1_e", data)
    x = mean_fixations(getattr(T, f"N{i}_P1_m")[0], getattr(T, f"N{i}_P1_m")[1], f"N{i}_P1_m", data)
    x = mean_fixations(getattr(T, f"N{i}_P1_h")[0], getattr(T, f"N{i}_P1_h")[1], f"N{i}_P1_h", data)

    # P2
    data = pd.read_csv(f"/Users/scottliu/Desktop/Peiran Processed Data/N{i}/N{i}_P2/fixations.csv")
    x = mean_fixations(getattr(T, f"N{i}_P2_e")[0], getattr(T, f"N{i}_P2_e")[1], f"N{i}_P2_e", data)
    x = mean_fixations(getattr(T, f"N{i}_P2_m")[0], getattr(T, f"N{i}_P2_m")[1], f"N{i}_P2_m", data)
    x = mean_fixations(getattr(T, f"N{i}_P2_h")[0], getattr(T, f"N{i}_P2_h")[1], f"N{i}_P2_h", data)
