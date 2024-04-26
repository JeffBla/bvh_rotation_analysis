import os
from pathlib import Path
import argparse

from config import videoDirPath_list

parser = argparse.ArgumentParser()
parser.add_argument("outputPath", type=str)

args = parser.parse_args()

outputPath = Path(args.outputPath)
outputPath.mkdir(exist_ok=True)

for videoDirPath, outputDirName in videoDirPath_list.items():
    videoDirPath = Path(videoDirPath).expanduser()

    outputDirPath = outputPath / outputDirName
    outputDirPath.mkdir(exist_ok=True)

    clipIdx = 1
    for videoPath in videoDirPath.glob("*.mp4"):
        videoName = videoPath.stem
        videoFullName = videoPath.name

        ProcessedDirPath = videoDirPath / (videoFullName + "-data")
        targetVideoPath = ProcessedDirPath / "2dJoints_v1.4.csv_lastRun3DHiRes.mp4"

        # Each video has its own output directory
        outputSequenceDirPath = outputDirPath / f"clip{clipIdx}"
        outputSequenceDirPath.mkdir(exist_ok=True)

        clipIdx += 1

        # Copy the video to the output directory
        outputVideoPath = outputSequenceDirPath / ("video" +
                                                   targetVideoPath.suffix)
        outputRefVideoPath = outputSequenceDirPath / ("video_ref" +
                                                      videoPath.suffix)
        os.system(f"cp {targetVideoPath} {outputVideoPath}")
        os.system(f"cp {videoPath} {outputRefVideoPath}")
