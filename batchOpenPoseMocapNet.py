import sys
import os
from pathlib import Path

videoDirPath = Path(sys.argv[1])
MocapNetConverterScriptPath = Path(sys.argv[2])

outputDirPath = videoDirPath / "output"
outputDirPath.mkdir(exist_ok=True)

for videoPath in videoDirPath.glob("*.mp4"):
    videoName = videoPath.stem
    ProcessedDirPath = outputDirPath / videoName + "-data"
    ProcessedCsvPath = ProcessedDirPath / "2dJoints_v1.4.csv"

    outputBvhPath = outputDirPath / (videoName + ".bvh")
    outputOpenPosePath = outputDirPath / (videoName + ".json")
    os.system(
        f"bash {MocapNetConverterScriptPath} {videoPath} {outputBvhPath}")
    os.system(f"cp {ProcessedCsvPath} {outputOpenPosePath}")
