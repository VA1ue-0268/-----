import os

# The path where the .ass subtitle files are located
subtitle_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6" # Update this path accordingly

# The path where you want to save the output .vtt files
output_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6" # Update this path accordingly

# The path where you want to save the commands to a .txt file
commands_file_path = "ffmpeg_commands_vtt.txt"

# Retrieve all .ass files in the subtitle folder
subtitle_files = [f for f in os.listdir(subtitle_folder_path) if f.endswith('.ass')]

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Open the file where we will write our commands
with open(commands_file_path, 'w') as cmd_file:
    # Write ffmpeg commands to convert each .ass file to .vtt
    for subtitle_file in subtitle_files:
        # Define the full path to the input and output files
        input_path = os.path.join(subtitle_folder_path, subtitle_file)
        output_file = os.path.splitext(subtitle_file)[0] + '.vtt'
        output_path = os.path.join(output_folder_path, output_file)
        
        # Write the ffmpeg command to the file
        command = f'ffmpeg -i "{input_path}" "{output_path}"\n'
        cmd_file.write(command)

# Returning the path to the commands file
commands_file_path
