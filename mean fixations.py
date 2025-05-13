import pandas as pd
from time_config import Time
T= Time()



def mean_fixations (minute=1, sec=1, label="x", data=pd.read_csv("/home/yulab/Desktop/N1/N1_P1/fixations.csv")):
    t_before_task_in_seconds =120
    t_after_task_in_seconds=120
    start_timestamp = data.iloc[0]['start timestamp [ns]']+ (minute * 60 + sec) * 1e9
    pretask_ns = start_timestamp - t_before_task_in_seconds * 1e9
    posttask_ns = start_timestamp+ t_after_task_in_seconds * 1e9
    interval = t_before_task_in_seconds+ t_after_task_in_seconds
    df = data[(data['start timestamp [ns]'] >= pretask_ns) & (data['end timestamp [ns]'] <= posttask_ns)]
    num_fixations = df["fixation id"].count()
    print(f"The mean fixations for {label} is {int(num_fixations) / interval} per second")

data = pd.read_csv("/home/yulab/Desktop/N1/N1_P1/fixations.csv")
x=mean_fixations(T.N1_P1_e[0], T.N1_P1_e[1], "N1_P1_e", data)


