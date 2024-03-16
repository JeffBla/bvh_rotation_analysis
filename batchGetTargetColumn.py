import sys
import os
from pathlib import Path
import numpy as np
import pandas as pd

target_column = "frameNumber	2DX_head	2DY_head	visible_head	2DX_neck	2DY_neck	visible_neck	2DX_rshoulder	2DY_rshoulder	visible_rshoulder	2DX_relbow	2DY_relbow	visible_relbow	2DX_rhand	2DY_rhand	visible_rhand	2DX_lshoulder	2DY_lshoulder	visible_lshoulder	2DX_lelbow	2DY_lelbow	visible_lelbow	2DX_lhand	2DY_lhand	visible_lhand	2DX_hip	2DY_hip	visible_hip	2DX_rhip	2DY_rhip	visible_rhip	2DX_rknee	2DY_rknee	visible_rknee	2DX_rfoot	2DY_rfoot	visible_rfoot	2DX_lhip	2DY_lhip	visible_lhip	2DX_lknee	2DY_lknee	visible_lknee	2DX_lfoot	2DY_lfoot	visible_lfoot	2DX_endsite_eye.r	2DY_endsite_eye.r	visible_endsite_eye.r	2DX_endsite_eye.l	2DY_endsite_eye.l	visible_endsite_eye.l	2DX_rear	2DY_rear	visible_rear	2DX_lear	2DY_lear	visible_lear	2DX_endsite_toe1-2.l	2DY_endsite_toe1-2.l	visible_endsite_toe1-2.l	2DX_endsite_toe5-3.l	2DY_endsite_toe5-3.l	visible_endsite_toe5-3.l	2DX_lheel	2DY_lheel	visible_lheel	2DX_endsite_toe1-2.r	2DY_endsite_toe1-2.r	visible_endsite_toe1-2.r	2DX_endsite_toe5-3.r	2DY_endsite_toe5-3.r	visible_endsite_toe5-3.r	2DX_rheel	2DY_rheel".split(
    "\t")

inputDirPath = Path(sys.argv[1])

for inputFilePath in inputDirPath.rglob("openpose.csv"):
    df = pd.read_csv(inputFilePath)
    df[target_column].to_csv(inputFilePath.with_name("openpose_target.csv"),
                             index=False)
