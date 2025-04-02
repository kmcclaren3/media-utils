
import os
from moviepy import VideoFileClip, concatenate_videoclips
import sys

def list_mp4_files(directory):
    mp4_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]
    return sorted(mp4_files)

def merge_mp4_files(files, output_file='merged.mp4'):
    clips = [VideoFileClip(file) for file in files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, codec='libx264')

def main():
    args = sys.argv[1:]

    if not args:
        directory = '.'
        files = list_mp4_files(directory)
    else:
        files = [arg for arg in args if os.path.isfile(arg) and arg.endswith('.mp4')]
        if not files:
            print('No valid .mp4 files provided. Retrieving from current directory...', file=sys.stderr)
            directory = '.'
            files = list_mp4_files(directory)

    if not files:
        print('No .mp4 files found.', file=sys.stderr)
        return

    if not merge_mp4_files(files):
        print('Failed to merge videos.', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
