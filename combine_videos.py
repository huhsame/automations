import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips


def combine_videos(start_index, num_pieces, output_filename, folder_path):
    # Load the videos from start_index for the specified number of pieces
    clips = [
        VideoFileClip(f"{folder_path}/{i}.mp4")
        for i in range(start_index, start_index + num_pieces)
    ]
    # Concatenate the video clips into one video, ensuring audio is included
    final_clip = concatenate_videoclips(clips, method="compose")
    # Write the result to a file
    final_clip.write_videofile(
        output_filename, codec="libx264", fps=24, audio_codec="aac"
    )
    # Close all the clips to free up resources
    for clip in clips:
        clip.close()


# Check if the folder path, number of pieces, and total number of files are provided
if len(sys.argv) < 4:
    print("Usage: python script_name.py [folder_path] [num_pieces] [total_files]")
    sys.exit(1)

folder_path = sys.argv[1]
num_pieces = int(sys.argv[2])
total_files = int(sys.argv[3])

# Validate the inputs
if num_pieces < 1 or total_files < num_pieces:
    print(
        "Invalid number of pieces or total files. Ensure num_pieces >= 1 and total_files >= num_pieces."
    )
    sys.exit(1)

# Main loop to process all videos
for i in range(1, total_files + 1, num_pieces):
    start_index = i
    end_index = min(i + num_pieces - 1, total_files)  # Prevent going out of range
    output_filename = (
        f"{folder_path}/combined_{(start_index + num_pieces - 1)//num_pieces}.mp4"
    )
    combine_videos(start_index, num_pieces, output_filename, folder_path)
