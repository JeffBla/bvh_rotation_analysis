#!/bin/bash

# Get the directory path as an argument
dir_path="$1"

# Check if directory path is provided
if [ -z "$dir_path" ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Go through each mp4 file in the directory
for file in "$dir_path"/*.mp4; do
    if [ -f "$file" ]; then
        # Extract file name and directory path
        file_name=$(basename "$file")
        directory=$(dirname "$file")

        # Replace spaces with underscores
        new_file_name="${file_name// /_}"

        # Rename the file
        mv "$file" "$directory/$new_file_name"

        echo "File name '$file' has been renamed to '$directory/$new_file_name'"
    fi
done
