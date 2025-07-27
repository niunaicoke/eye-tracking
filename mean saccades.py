import pandas as pd
from time_config import Time
T= Time()
import os
import pandas as pd
import numpy as np

def save_results_to_csv(filename="mean_saccades.csv"):
    if not hasattr(mean_saccades, 'results_dict') or not mean_saccades.results_dict:
        print("没保存的结果数据")
        return
    results_df = pd.DataFrame(
        list(mean_saccades.results_dict.items()),
        columns=['variable', 'value']
    )
    if 'value' in results_df.columns:
        valid_values = results_df['value'].replace(0, np.nan).dropna()
        col_mean = valid_values.mean() if not valid_values.empty else 0
        col_mean = round(col_mean, 3)
        results_df['value'] = results_df['value'].apply(
            lambda x: col_mean if (pd.isna(x) or x == 0) else x
        )
    results_df.to_csv(filename, index=False, encoding='utf-8')
    print(f"结果已保存至: {os.path.abspath(filename)}")


def mean_saccades (minute=1, sec=1, label="x", data=""):
    t_before_task_in_seconds =60
    t_after_task_in_seconds=120
    start_timestamp = data.iloc[0]['start timestamp [ns]']+ (minute * 60 + sec) * 1e9
    pretask_ns = start_timestamp - t_before_task_in_seconds * 1e9
    posttask_ns = start_timestamp+ t_after_task_in_seconds * 1e9
    interval = t_before_task_in_seconds+ t_after_task_in_seconds
    df = data[(data['start timestamp [ns]'] >= pretask_ns) & (data['end timestamp [ns]'] <= posttask_ns)]
    num_saccades = df["saccade id"].count()
    result = round(int(num_saccades) / interval, 3)
    print(f"The mean saccades for {label} is {result} per second")
    if not hasattr(mean_saccades, 'results_dict'):
        mean_saccades.results_dict = {}
    mean_saccades.results_dict[label] = result


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


print("################################################")



for i in range(1, 10):
    # P1
    data = pd.read_csv(f"/Users/scottliu/Desktop/Peiran Processed Data/E{i}/E{i}_P1/saccades.csv")
    x = mean_saccades(getattr(T, f"E{i}_P1_e")[0], getattr(T, f"E{i}_P1_e")[1], f"E{i}_P1_e", data)
    x = mean_saccades(getattr(T, f"E{i}_P1_m")[0], getattr(T, f"E{i}_P1_m")[1], f"E{i}_P1_m", data)
    x = mean_saccades(getattr(T, f"E{i}_P1_h")[0], getattr(T, f"E{i}_P1_h")[1], f"E{i}_P1_h", data)

    # P2
    data = pd.read_csv(f"/Users/scottliu/Desktop/Peiran Processed Data/E{i}/E{i}_P2/saccades.csv")
    x = mean_saccades(getattr(T, f"E{i}_P2_e")[0], getattr(T, f"E{i}_P2_e")[1], f"E{i}_P2_e", data)
    x = mean_saccades(getattr(T, f"E{i}_P2_m")[0], getattr(T, f"E{i}_P2_m")[1], f"E{i}_P2_m", data)
    x = mean_saccades(getattr(T, f"E{i}_P2_h")[0], getattr(T, f"E{i}_P2_h")[1], f"E{i}_P2_h", data)





save_results_to_csv()