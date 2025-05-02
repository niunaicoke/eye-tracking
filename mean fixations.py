import pandas as pd
from time_config import Time
T= Time()



def mean_fixations (t_before_task_in_seconds =60, t_after_task_in_seconds=60, minute=1, sec=1, label="x", data=pd.read_csv("/home/yulab/Desktop/N1/N1_P1/fixations.csv")):
    start_timestamp = data.iloc[0]['start timestamp [ns]']
    start_offset_ns = (minute * 60 + sec+ t_before_task_in_seconds) * 1e9
    end_offset_ns = (minute * 60 + sec + t_after_task_in_seconds) * 1e9
    start_time_ns = start_timestamp - start_offset_ns
    end_time_ns = start_timestamp + end_offset_ns
    interval = t_before_task_in_seconds+ t_after_task_in_seconds
    N1_P1_e = data[(data['start timestamp [ns]'] >= start_time_ns) & (data['end timestamp [ns]'] <= end_time_ns)]
    N1_P1_e = N1_P1_e["fixation id"].count()
    print(f"The mean fixations for {label} is {int(N1_P1_e) / interval} per second")

data = pd.read_csv("/home/yulab/Desktop/N1/N1_P1/fixations.csv")
x=mean_fixations(60,60, T.N1_P1_e[0], T.N1_P1_e[1], "N1_P1_e", data)


