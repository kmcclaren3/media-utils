import argparse

from moviepy import VideoFileClip


def extract_clip(input_file, start_time, end_time, output_file):
    # Load the video file
    video_clip = VideoFileClip(input_file)

    # Convert the time strings to seconds
    start_seconds = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
    end_seconds = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])

    # Extract the clip
    clip = video_clip.subclipped(start_seconds, end_seconds)

    # Save the clip to a new file
    clip.write_videofile(output_file)

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Extract a clip from a video file based on timestamps.")

    # Add arguments for input file, start time, end time, and output file
    parser.add_argument('input_file', type=str, help='Path to the input .mp4 file')
    parser.add_argument('start_time', type=str, help='Start time of the clip in mm:ss format')
    parser.add_argument('end_time', type=str, help='End time of the clip in mm:ss format')
    parser.add_argument('output_file', type=str, help='Path to save the extracted clip')

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    extract_clip(args.input_file, args.start_time, args.end_time, args.output_file)
