import os

# Define the paths to the video files and subtitle files
# You must replace these with the actual paths on your local system
video_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6"  # Replace with the path to your video files
subtitle_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6"  # Replace with the path to your subtitle files
output_folder_path = "G:\ptsbao\My Little Pony Friendship is Magic Seasons 1-9 Compete Series 1080p Web DL H264\Season 6"  # Replace with the path where you want the output MP4 files

# List out all the video and subtitle files in order
video_files = sorted([file for file in os.listdir(video_folder_path) if file.endswith('.mkv')])
subtitle_files = sorted([file for file in os.listdir(subtitle_folder_path) if file.endswith('.ass')])

# Check if video files and subtitle files count matches
if len(video_files) != len(subtitle_files):
    raise ValueError("The number of video files and subtitle files does not match.")

# Define the output text file path
output_commands_file = os.path.join(output_folder_path, 'ffmpeg_commands.txt')

# Generate FFmpeg commands and save them to the text file
with open(output_commands_file, 'w') as file:
    for video, subtitle in zip(video_files, subtitle_files):
        video_path = os.path.join(video_folder_path, video)
        subtitle_path = os.path.join(subtitle_folder_path, subtitle)
        output_video = os.path.splitext(video)[0] + '.mp4'
        output_video_path = os.path.join(output_folder_path, output_video)
        
        command = f'.\\ffmpeg.exe -i "{video_path}" -map 0:v -map 0:a:1 -c:v copy -c:a copy "{output_video_path}"'
        #command = f'.\\ffmpeg.exe -hwaccel cuda -i "{video_path}" -map 0:v -map 0:a:1 -c:v h264_nvenc -preset fast -c:a copy "{output_video_path}"'
        #-preset fast：指定编码预设（preset），可以调整为 slow, medium, fast 等，以在编码速度和质量之间取得平衡。
        file.write(command + '\n')

print(f'FFmpeg commands have been written to {output_commands_file}.')
