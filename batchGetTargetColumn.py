import sys
import os
from pathlib import Path
import numpy as np
import pandas as pd
import argparse

target_column = "frameNumber	2DX_head	2DY_head	2DX_neck	2DY_neck	2DX_rshoulder	2DY_rshoulder	2DX_relbow	2DY_relbow	2DX_rhand	2DY_rhand	2DX_lshoulder	2DY_lshoulder	2DX_lelbow	2DY_lelbow	2DX_lhand	2DY_lhand	2DX_hip	2DY_hip	2DX_rhip	2DY_rhip	2DX_rknee	2DY_rknee	2DX_rfoot	2DY_rfoot	2DX_lhip	2DY_lhip	2DX_lknee	2DY_lknee	2DX_lfoot	2DY_lfoot	2DX_lheel	2DY_lheel	2DX_rheel	2DY_rheel".split(
    "\t")


def GetTargetColumnFromFileToFile(target_filepath, output_filepath):
    df = pd.read_csv(target_filepath)
    df[target_column].to_csv(output_filepath, index=False)


if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputDirPath", type=str)

    args = argparser.parse_args()

    inputDirPath = Path(args.inputDirPath)
    for inputFilePath in inputDirPath.rglob("openpose.csv"):
        df = pd.read_csv(inputFilePath)
        df[target_column].to_csv(
            inputFilePath.with_name("openpose_target.csv"), index=False)
