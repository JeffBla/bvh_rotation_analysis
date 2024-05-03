import re

videoDirPath_list = {
    "~/Video/bvh_analysis/bigman_edit": "bigman",
    "~/Video/bvh_analysis/me_edit/clip1_correct": "me1",
    "~/Video/bvh_analysis/me_edit/clip4_wrong": "me4",
    "~/Video/bvh_analysis/me_edit/clip5": "me5",
    "~/Video/bvh_analysis/rookie_edit/rookie2": "rookie2",
    "~/Video/bvh_analysis/small_rotation_edit": "small_rotation",
    "~/Video/bvh_analysis/finalTest": "finalTest"
}

output_with_angle_path = [
    "~/Video/bvh_analysis/output/bigman", "~/Video/bvh_analysis/output/me1",
    "~/Video/bvh_analysis/output/me4", "~/Video/bvh_analysis/output/me5",
    "~/Video/bvh_analysis/output/rookie2",
    "~/Video/bvh_analysis/output/small_rotation",
    "~/Video/bvh_analysis/output/finalTest"
]


def natural_sort(l):
    atoi = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [
        atoi(c) for c in re.split('([0-9]+)', str(key))
    ]
    return sorted(l, key=alphanum_key)
