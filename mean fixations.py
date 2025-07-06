import pandas as pd
from time_config import Time
T= Time()



def mean_fixations (minute=1, sec=1, label="x",data_path=""):
    t_before_task_in_seconds =120
    t_after_task_in_seconds=120
    start_timestamp = data_path.iloc[0]['start timestamp [ns]']+ (minute * 60 + sec) * 1e9
    pretask_ns = start_timestamp - t_before_task_in_seconds * 1e9
    posttask_ns = start_timestamp+ t_after_task_in_seconds * 1e9
    interval = t_before_task_in_seconds+ t_after_task_in_seconds
    df = data_path[(data_path['start timestamp [ns]'] >= pretask_ns) & (data_path['end timestamp [ns]'] <= posttask_ns)]
    num_fixations = df["fixation id"].count()
    print(f"The mean fixations for {label} is {int(num_fixations) / interval} per second")



# #N1
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N1/N1_P1/fixations.csv")
# x=mean_fixations(T.N1_P1_e[0], T.N1_P1_e[1], "N1_P1_e", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N1/N1_P1/fixations.csv")
# x=mean_fixations(T.N1_P1_m[0], T.N1_P1_m[1], "N1_P1_m", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N1/N1_P1/fixations.csv")
# x=mean_fixations(T.N1_P1_h[0], T.N1_P1_h[1], "N1_P1_h", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N1/N1_P2/fixations.csv")
# x = mean_fixations(T.N1_P2_e[0], T.N1_P2_e[1], "N1_P2_e", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N1/N1_P2/fixations.csv")
# x = mean_fixations(T.N1_P2_m[0], T.N1_P2_m[1], "N1_P2_m", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N1/N1_P2/fixations.csv")
# x = mean_fixations(T.N1_P2_h[0], T.N1_P2_h[1], "N1_P2_h", data)
#
#
# #N2
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N2/N2_P1/fixations.csv")
# x=mean_fixations(T.N2_P1_e[0], T.N2_P1_e[1], "N2_P1_e", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N2/N2_P1/fixations.csv")
# x=mean_fixations(T.N2_P1_m[0], T.N2_P1_m[1], "N2_P1_m", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N2/N2_P1/fixations.csv")
# x=mean_fixations(T.N2_P1_h[0], T.N2_P1_h[1], "N2_P1_h", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N2/N2_P2/fixations.csv")
# x = mean_fixations(T.N2_P2_e[0], T.N2_P2_e[1], "N2_P2_e", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N2/N2_P2/fixations.csv")
# x = mean_fixations(T.N2_P2_m[0], T.N2_P2_m[1], "N2_P2_m", data)
#
# data = pd.read_csv("/Users/scottliu/Desktop/Peiran Processed Data/N2/N2_P2/fixations.csv")
# x = mean_fixations(T.N2_P2_h[0], T.N2_P2_h[1], "N2_P2_h", data)


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