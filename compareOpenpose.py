import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.graph_objects as go

from tslearn.metrics import lcss_path
from tslearn.utils import to_time_series_dataset
from tslearn.preprocessing import TimeSeriesResampler

from visualizeOpenpose import readOpenposeJointsCSV

filenames = [
    'test/ref.csv',
    'test/test.csv',
]

df1 = readOpenposeJointsCSV(filenames[0])
df2 = readOpenposeJointsCSV(filenames[1])

num_frame = max(df1.count().max(), df2.count().max())

ts1 = TimeSeriesResampler(sz=num_frame).fit_transform(df1['std'].values)
ts2 = TimeSeriesResampler(sz=num_frame).fit_transform(df2['std'].values)

# ts1 = df1['std'].values
# ts2 = df2['std'].values

# dataset_scaled = to_time_series_dataset([ts1, ts2])

dataset_scaled = np.concatenate([ts1, ts2])

my_lcss_path, sim_lcss = lcss_path(dataset_scaled[0, :, 0],
                                   dataset_scaled[1, :, 0],
                                   eps=0.5)

print(sim_lcss)

plt.figure(1, figsize=(8, 8))

plt.plot(dataset_scaled[0, :, 0], "b-", label='small_rotation_clip1')
plt.plot(dataset_scaled[1, :, 0], "g-", label='me_downPush')

for positions in my_lcss_path:
    plt.plot([positions[0], positions[1]], [
        dataset_scaled[0, positions[0], 0], dataset_scaled[1, positions[1], 0]
    ],
             color='orange')

# plt.plot([my_lcss_path[i][0] for i in range(len(my_lcss_path))], "r-", label='LCSS path')

plt.legend()
plt.title("Time series matching with LCSS")

plt.tight_layout()
plt.show()
