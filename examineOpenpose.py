import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data/2dJoints_v1.4.csv')

df_rshoulder_x = df['2DX_rshoulder']
df_rshoulder_y = df['2DY_rshoulder']

df_lshoulder_x = df['2DX_lshoulder']
df_lshoulder_y = df['2DY_lshoulder']

df_dist = pd.DataFrame(np.abs(df_rshoulder_y - df_lshoulder_y),
                       columns=["dist_y"])

df_dist["std"] = (df_dist["dist_y"] -
                  df_dist["dist_y"].mean()) / df_dist["dist_y"].std()

fig = px.line(df_dist["std"], markers=True)
fig.add_trace(
    go.Scatter(x=df_dist.index,
               y=df_dist["dist_y"],
               mode='lines',
               label='dist_y'))
fig.show()
