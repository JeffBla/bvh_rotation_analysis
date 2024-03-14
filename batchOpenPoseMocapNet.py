import sys
import os
from pathlib import Path

videoDirPath_list = [
    "~/Video/bvh_analysis/bigman_edit",
    "~/Video/bvh_analysis/me_edit/clip1_correct",
    "~/Video/bvh_analysis/me_edit/clip4_wrong",
    "~/Video/bvh_analysis/me_edit/clip5",
    "~/Video/bvh_analysis/rookie_edit/rookie2",
    "~//Video/bvh_analysis/small_rotation_edit"
]

MocapNetConverterScriptPath = Path(sys.argv[1])

outputPath = Path(sys.argv[2])
outputPath.mkdir(exist_ok=True)

for videoDirPath in videoDirPath_list:
    videoDirPath = Path(videoDirPath).expanduser()

    outputDirPath = outputPath / videoDirPath.name
    outputDirPath.mkdir(exist_ok=True)

    # Format file(replace the space in the file name with underscore)
    os.system(f"bash ./formatFile.sh {videoDirPath}")

    for videoPath in videoDirPath.glob("*.mp4"):
        videoName = videoPath.stem
        videoFullName = videoPath.name

        # Each video has its own output directory
        outputSequenceDirPath = outputDirPath / videoName
        outputSequenceDirPath.mkdir(exist_ok=True)

        outputBvhPath = outputSequenceDirPath / (videoName + ".bvh")
        os.system(
            f"bash {MocapNetConverterScriptPath} {videoPath} {outputBvhPath}")

        ProcessedDirPath = videoDirPath / (videoFullName + "-data")
        ProcessedCsvPath = ProcessedDirPath / "2dJoints_v1.4.csv"
        outputOpenPosePath = outputSequenceDirPath / (videoName + ".csv")
        os.system(f"cp {ProcessedCsvPath} {outputOpenPosePath}")
