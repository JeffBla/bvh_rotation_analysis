#!/bin/bash

################## Input Example ##############################
# bash renameFile.sh /home/jeffbla/Video/bvh_analysis/output/ #
###############################################################

# Function to rename CSV files
rename_csv() {
    local directory="$1"
    # Rename CSV files in the directory
    # This is a bash parameter expansion syntax used to extract the directory part of the file path.
    # ${0%/*} means to remove everything after the last / in the file path.
    find "$directory" -type f -name "$(basename $directory).csv" -exec bash -c 'mv "$0" "${0%/*}/openpose.csv"' {} \;
}

# Main function to traverse directories
traverse_directories() {
    local parent_dir="$1"
    local dirs=("$parent_dir"/*/)

    # Loop through each subdirectory
    for dir in "${dirs[@]}"; do
        if [ -d "$dir" ]; then
            # Rename CSV files in the current directory
            rename_csv "$dir"
            # Recursively traverse subdirectories
            traverse_directories "$dir"
        fi
    done
}

# Check if the target directory is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <target_directory>"
    exit 1
fi

target_directory="$1"

# Check if the target directory exists
if [ ! -d "$target_directory" ]; then
    echo "Error: Target directory '$target_directory' does not exist."
    exit 1
fi

# Rename CSV files in the target directory
traverse_directories "$target_directory"

echo "All CSV files in '$target_directory' renamed to 'openpose.csv'."
