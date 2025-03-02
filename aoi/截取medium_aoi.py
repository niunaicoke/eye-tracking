import pandas as pd

fixations_df = pd.read_csv("/Users/scottliu/Desktop/1+2/medium_step_test/fixations.csv")
fixation_ids = set(fixations_df["fixation id"].unique())
aoi_fixations_df = pd.read_csv("/Users/scottliu/Desktop/Protocol_4_MARKER-MAPPER_Emma_1,_first_video_csv/aoi_fixations.csv")
aoi_filtered_df = aoi_fixations_df[aoi_fixations_df["fixation id"].isin(fixation_ids)]
aoi_filtered_df.to_csv("/Users/scottliu/Desktop/1+2_aoi/medium_aoi.csv", index=False)

print("筛选完成，结果保存在 medium_aoi.csv")
