import pandas as pd
from time_config import Time
T= Time()



def mean_saccades (minute=1, sec=1, label="x", data=""):
    t_before_task_in_seconds =120
    t_after_task_in_seconds=120
    start_timestamp = data.iloc[0]['start timestamp [ns]']+ (minute * 60 + sec) * 1e9
    pretask_ns = start_timestamp - t_before_task_in_seconds * 1e9
    posttask_ns = start_timestamp+ t_after_task_in_seconds * 1e9
    interval = t_before_task_in_seconds+ t_after_task_in_seconds
    df = data[(data['start timestamp [ns]'] >= pretask_ns) & (data['end timestamp [ns]'] <= posttask_ns)]
    num_saccades = df["saccade id"].count()
    print(f"The mean saccades for {label} is {int(num_saccades) / interval} per second")


for i in range(1, 10):
    # P1
    data = pd.read_csv(f"/Users/scottliu/Desktop/Peiran Processed Data/N{i}/N{i}_P1/saccades.csv")
    x = mean_saccades(getattr(T, f"N{i}_P1_e")[0], getattr(T, f"N{i}_P1_e")[1], f"N{i}_P1_e", data)
    x = mean_saccades(getattr(T, f"N{i}_P1_m")[0], getattr(T, f"N{i}_P1_m")[1], f"N{i}_P1_m", data)
    x = mean_saccades(getattr(T, f"N{i}_P1_h")[0], getattr(T, f"N{i}_P1_h")[1], f"N{i}_P1_h", data)

    # P2
    data = pd.read_csv(f"/Users/scottliu/Desktop/Peiran Processed Data/N{i}/N{i}_P2/saccades.csv")
    x = mean_saccades(getattr(T, f"N{i}_P2_e")[0], getattr(T, f"N{i}_P2_e")[1], f"N{i}_P2_e", data)
    x = mean_saccades(getattr(T, f"N{i}_P2_m")[0], getattr(T, f"N{i}_P2_m")[1], f"N{i}_P2_m", data)
    x = mean_saccades(getattr(T, f"N{i}_P2_h")[0], getattr(T, f"N{i}_P2_h")[1], f"N{i}_P2_h", data)


