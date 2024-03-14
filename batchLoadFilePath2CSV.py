import re
import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd


def natural_sort(l):
    atoi = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [
        atoi(c) for c in re.split('([0-9]+)', str(key))
    ]
    return sorted(l, key=alphanum_key)


inputDirPath = Path(sys.argv[1])
outputPath = Path(sys.argv[2])

outputFilename = "annotation_file.csv"

columns = [
    "openpose_files", "angle_files", "waist_twist_correct",
    "waist_twist_aggressively", "waist_no_twist", "forhand_correct",
    "forehand_wave_aggressively", "forehand_no_wave"
]

# Load the openpose file path
df = pd.DataFrame(columns=columns)

df["openpose_files"] = list(natural_sort(inputDirPath.rglob("openpose.csv")))

df.to_csv(outputPath / outputFilename, index=False)
