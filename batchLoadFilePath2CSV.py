import os
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

from config import natural_sort

parser = argparse.ArgumentParser()
parser.add_argument("inputDirPath", type=str)
parser.add_argument("outputPath", type=str)
parser.add_argument("--inputFile", type=str)
parser.add_argument('--is_input_xlsx', action=argparse.BooleanOptionalAction)
parser.add_argument('--is_input_angle', action=argparse.BooleanOptionalAction)

args = parser.parse_args()
inputDirPath = Path(args.inputDirPath)
outputPath = Path(args.outputPath)

outputFilename = "annotation_file.csv"

columns = [
    "openpose_files", "angle_files", "waist_twist_correct",
    "waist_twist_aggressively", "waist_no_twist", "forhand_correct",
    "forehand_wave_aggressively", "forehand_no_wave"
]

if args.is_input_xlsx and args.inputFile is not None:
    # Load the xlsx file path
    df = pd.read_excel(args.inputFile)
elif args.inputFile is not None:
    # Load the csv file path
    df = pd.read_csv(args.inputFile)
else:
    df = pd.DataFrame(columns=columns)

df["openpose_files"] = list(
    natural_sort(inputDirPath.rglob("openpose_target.csv")))

if args.is_input_angle:
    df["angle_files"] = list(
        natural_sort(inputDirPath.rglob("forehand_stroke.csv")))

df.to_csv(outputPath / outputFilename, index=False)
