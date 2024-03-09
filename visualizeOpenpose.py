import pandas as pd
import numpy as np

import plotly.graph_objects as go


def readOpenposeJointsCSV(filename):
    df = pd.read_csv(filename)

    df_rshoulder_x = df['2DX_rshoulder']

    df_lshoulder_x = df['2DX_lshoulder']

    df_dist = pd.DataFrame(np.abs(df_rshoulder_x - df_lshoulder_x),
                           columns=["dist_y"])

    df_dist["std"] = (df_dist["dist_y"] -
                      df_dist["dist_y"].mean()) / df_dist["dist_y"].std()
    return df_dist


if __name__ == "__main__":

    filenames = [
        'data_openpose/bigman_22/2dJoints_v1.4.csv',
        'data_openpose/me_noMoveElbow/2dJoints_v1.4.csv',
        'data_openpose/proficient_bigman/2dJoints_v1.4.csv',
        'data_openpose/small_rotation_clip1/2dJoints_v1.4.csv'
    ]

    fig = go.Figure()

    for filename in filenames:
        df = pd.read_csv(filename)

        df_rshoulder_x = df['2DX_rshoulder']

        df_lshoulder_x = df['2DX_lshoulder']

        df_dist = pd.DataFrame(np.abs(df_rshoulder_x - df_lshoulder_x),
                               columns=["dist_y"])

        df_dist["std"] = (df_dist["dist_y"] -
                          df_dist["dist_y"].mean()) / df_dist["dist_y"].std()

        filename = filename.split('/')[-2]
        fig.add_trace(
            go.Scatter(x=df_dist.index,
                       y=df_dist["std"],
                       mode='lines',
                       name=f'{filename}_std'))
        fig.add_trace(
            go.Scatter(x=df_dist.index,
                       y=df_dist["dist_y"],
                       mode='lines',
                       name=f'{filename}_dist_y'))
    fig.show()
