import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tslearn.metrics import lcss_path
from tslearn.utils import to_time_series_dataset
from tslearn.preprocessing import TimeSeriesScalerMeanVariance, TimeSeriesResampler

whole_data_df0 = pd.read_csv('data/bigman_22/whole_body.csv')
whole_data_df1 = pd.read_csv(
    'data/small_rotation_clip1_edit.mp4-data/whole_body.csv')

whole_data_dfs = [whole_data_df0, whole_data_df1]

whole_data_ts_list = {}

max_frame = 0
for whole_data_df in whole_data_dfs:
    max_frame = max(whole_data_df['frame'].max(), max_frame)

scaler = TimeSeriesScalerMeanVariance(mu=0., std=1.)  # Rescale time series
for header in whole_data_df.columns:
    if np.isnan(whole_data_df[header].values[0]):
        continue
    ts1 = TimeSeriesResampler(sz=max_frame).fit_transform(
        whole_data_dfs[0][header].values)
    ts2 = TimeSeriesResampler(sz=max_frame).fit_transform(
        whole_data_dfs[1][header].values)
    dataset_scaled = scaler.fit_transform(np.concatenate([ts1, ts2]))
    whole_data_ts_list[header] = dataset_scaled
for key, dataset in whole_data_ts_list.items():
    my_lcss_path, sim_lcss = lcss_path(dataset[0, :, 0],
                                       dataset[1, :, 0],
                                       eps=0.5)

    print(key)
    print(sim_lcss)

    plt.figure(1, figsize=(8, 8))

    plt.plot(dataset[0, :, 0], "b-", label='bigman_22 time series')
    plt.plot(dataset[1, :, 0], "g-", label='small_rotation_clip1 time series')

    for positions in my_lcss_path:
        plt.plot([positions[0], positions[1]],
                 [dataset[0, positions[0], 0], dataset[1, positions[1], 0]],
                 color='orange')

    # plt.plot([my_lcss_path[i][0] for i in range(len(my_lcss_path))], "r-", label='LCSS path')

    plt.legend()
    plt.title("Time series matching with LCSS")

    plt.tight_layout()
    plt.show()
