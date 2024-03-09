import pandas as pd
import numpy as np

from sklearn.utils import resample

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from tslearn.metrics import lcss_path
from tslearn.utils import to_time_series_dataset
from tslearn.preprocessing import TimeSeriesScalerMeanVariance

whole_data_df0 = pd.read_csv('data/bigman_22/whole_body.csv')
whole_data_df1 = pd.read_csv('data/me_clip8.mp4-data/whole_body.csv')
whole_data_df2 = pd.read_csv('data/rookie2_clip1.mp4-data/whole_body.csv')
whole_data_df3 = pd.read_csv(
    'data/small_rotation_clip1_edit.mp4-data/whole_body.csv')
whole_data_df4 = pd.read_csv('data/me_noMoveElbow/whole_body.csv')

# whole_data_dfs = [
#     whole_data_df0, whole_data_df1, whole_data_df2, whole_data_df3
# ]

whole_data_dfs = [whole_data_df4]

fig = make_subplots(rows=len(whole_data_dfs),
                    cols=1,
                    shared_xaxes=True,
                    subplot_titles=[
                        'bigman_22', 'me_clip8', 'rookie2_clip1',
                        'small_rotation_clip1'
                    ])

max_frame = 0
for whole_data_df in whole_data_dfs:
    max_frame = max(whole_data_df['frame'].max(), max_frame)

for idx, whole_data_df in enumerate(whole_data_dfs):
    resample(whole_data_df, n_samples=max_frame, replace=True, random_state=0)
    for header in whole_data_df.columns:
        fig.add_trace(go.Scatter(x=whole_data_df['frame'],
                                 y=whole_data_df[header],
                                 mode='lines',
                                 name=header),
                      row=idx + 1,
                      col=1)
fig.show()
