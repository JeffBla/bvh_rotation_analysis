# Description: This script is used to collect the angle of the skeleton with the Application GUI
# My screen resolution is 1920x1080
# x: 0 to 1919
# y: 0 to 1079

import os
import time
import pyautogui
import argparse
from pathlib import Path

from config import output_with_angle_path, natural_sort

DELAY = 0.01


# Test the position of the mouse
def TestMousePosition():
    while True:
        print(pyautogui.position())
        pyautogui.sleep(1)


def StartMouseMotionWithFileContent(file_content, motion_file_path,
                                    video_file_path, openpose_file_path):
    tmp_content = file_content.replace("BVH_MOTION_FILE_PATH",
                                       str(motion_file_path))
    tmp_content = tmp_content.replace("VIDEO_FILE_PATH", str(video_file_path))
    tmp_content = tmp_content.replace("OPENPOSE_FILE_PATH",
                                      str(openpose_file_path))
    lines = tmp_content.split('\n')
    for line in lines:
        if line == "import pyautogui" or line == "import time" or line == "":
            continue
        eval(line)
        time.sleep(DELAY)


def StartMouseMotion(motion_template, motion_file_path, video_file_path,
                     openpose_file_path):
    f = open(motion_template, "r")
    lines = f.readlines()
    for line in lines:
        if line == "import pyautogui\n" or line == "import time\n" or line == "\n":
            continue
        # Replace the motion file path
        line = line.replace("BVH_MOTION_FILE_PATH", str(motion_file_path))
        # Replace the video file path
        line = line.replace("VIDEO_FILE_PATH", str(video_file_path))
        # Replace the openpose file path
        line = line.replace("OPENPOSE_FILE_PATH", str(openpose_file_path))
        line = line.strip('\n')
        eval(line)
        time.sleep(DELAY)
    f.close()


if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument("inputDirPath", type=str)
    argparser.add_argument("--isTestMousePosition",
                           action=argparse.BooleanOptionalAction)

    args = argparser.parse_args()

    if args.isTestMousePosition:
        while True:
            TestMousePosition()
        exit()

    mouseControllerTemplate = "./asset/motionTemplate"
    afterAnaysisOuput = Path(
        "~/Project/bvh_analysis_viewer_withEngine/cmake-build-debug/output/forehand_stroke.csv"
    )

    motion_template_file = open(mouseControllerTemplate, "r")
    motion_template = motion_template_file.read()
    motion_template_file.close()

    inputDirPath = Path(args.inputDirPath)
    for openposeFilePath in natural_sort(
            inputDirPath.rglob("openpose_target.csv")):
        openposeFilePath = Path(openposeFilePath)
        targetDir = openposeFilePath.parent
        motionFilePath = targetDir / "motion.bvh"
        videoFilePath = targetDir / "video.mp4"
        StartMouseMotionWithFileContent(motion_template, motionFilePath,
                                        videoFilePath, openposeFilePath)
        # Copy the output file to the target directory
        os.system(
            f"cp {afterAnaysisOuput} {targetDir / afterAnaysisOuput.name}")
