import sys
import os
from pathlib import Path
import argparse

from config import videoDirPath_list
from batchGetTargetColumn import GetTargetColumnFromFileToFile

parser = argparse.ArgumentParser()
parser.add_argument("MocapNetConverterScriptPath", type=str)
parser.add_argument("outputPath", type=str)
parser.add_argument("--isGetTargetColumn",
                    action=argparse.BooleanOptionalAction)

args = parser.parse_args()

MocapNetConverterScriptPath = Path(args.MocapNetConverterScriptPath)

outputPath = Path(args.outputPath)
outputPath.mkdir(exist_ok=True)

for videoDirPath, outputDirName in videoDirPath_list.items():
    videoDirPath = Path(videoDirPath).expanduser()

    outputDirPath = outputPath / outputDirName
    outputDirPath.mkdir(exist_ok=True)

    # Format file(replace the space in the file name with underscore)
    os.system(f"bash ./formatMp4File.sh {videoDirPath}")

    clipIdx = 0
    for videoPath in videoDirPath.glob("*.mp4"):
        videoFullName = videoPath.name

        # Each video has its own output directory
        outputSequenceDirPath = outputDirPath / ("clip" + str(clipIdx))
        outputSequenceDirPath.mkdir(exist_ok=True)

        outputBvhPath = outputSequenceDirPath / ("motion.bvh")
        os.system(
            f"bash {MocapNetConverterScriptPath} {videoPath} {outputBvhPath}")

        ProcessedDirPath = videoDirPath / (videoFullName + "-data")
        ProcessedCsvPath = ProcessedDirPath / "2dJoints_v1.4.csv"
        outputOpenPosePath = outputSequenceDirPath / ("openpose.csv")
        os.system(f"cp {ProcessedCsvPath} {outputOpenPosePath}")
        if args.isGetTargetColumn:
            outputOpenPoseTargetPath = outputSequenceDirPath / "openpose_target.csv"
            GetTargetColumnFromFileToFile(outputOpenPosePath,
                                          outputOpenPoseTargetPath)

        # Copy the video to the output directory
        targetVideoPath = ProcessedDirPath / "2dJoints_v1.4.csv_lastRun3DHiRes.mp4"
        outputVideoPath = outputSequenceDirPath / ("video" + videoPath.suffix)
        outputRefVideoPath = outputSequenceDirPath / ("video_ref" +
                                                      videoPath.suffix)
        os.system(f"cp {targetVideoPath} {outputVideoPath}")
        os.system(f"cp {videoPath} {outputRefVideoPath}")
