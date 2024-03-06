import os

# Assuming the current directory contains the subtitle files and they need to be renamed.
# This path should be updated to where the user has stored their subtitle files.
subtitle_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6"

# List all subtitle files in the directory
subtitle_files = [f for f in sorted(os.listdir(subtitle_folder_path)) if f.endswith('.ass')]

# Define a function to rename subtitles to match the video files
def rename_subtitles(subtitle_files, video_folder_path):
    # List all video files in the directory and sort them
    video_files = [f for f in sorted(os.listdir(video_folder_path)) if f.endswith('.mkv')]

    # Check if the number of subtitle files matches the number of video files
    if len(subtitle_files) != len(video_files):
        return "The number of subtitle files does not match the number of video files."
    
    # Generate new subtitle names based on video file names
    rename_commands = []
    for video_file, subtitle_file in zip(video_files, subtitle_files):
        # Extract the base name without extension and add '_en.ass'
        new_subtitle_name = os.path.splitext(video_file)[0] + '_en.ass'
        old_subtitle_path = os.path.join(subtitle_folder_path, subtitle_file)
        new_subtitle_path = os.path.join(subtitle_folder_path, new_subtitle_name)

        # Generate the mv (move) command to rename files, used for Unix-based systems
        command = f'mv "{old_subtitle_path}" "{new_subtitle_path}"'
        rename_commands.append((old_subtitle_path, new_subtitle_path))

    return rename_commands

# This is the path where the video files are located.
# The user will need to update this path to match their file structure.
video_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6"

# Call the function to get rename commands
rename_commands = rename_subtitles(subtitle_files, video_folder_path)

# Execute the rename operations
for old_name, new_name in rename_commands:
    os.rename(old_name, new_name)

# Return the list of new file names to confirm the rename operation