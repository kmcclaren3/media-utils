
import sys, os
import numpy as np
from PIL import Image

def main():
    if len(sys.argv) != 3:
        print("Usage: python slowdown_video.py <input_file.mp4> <slowdown_percentage>")
        return

    input_file = sys.argv[1]
    try:
        slowdown_percentage = float(sys.argv[2])
        if slowdown_percentage <= 0 or slowdown_percentage >= 1:
            raise ValueError
    except (ValueError, TypeError):
        print("Invalid slowdown percentage. It must be a floating point number between 0 and 1.")
        return

    # Ensure the input file exists
    if not os.path.isfile(input_file) or not input_file.endswith('.mp4'):
        print(f"File '{input_file}' does not exist or is not an .mp4 file.")
        return

    try:
        frames = []
        with open(input_file, 'rb') as f:
            while True:
                frame_data = f.read(1920 * 1080 * 3)  # Assuming RGB format
                if not frame_data:
                    break
                frame = Image.frombuffer('RGB', (1920, 1080), frame_data)
                frames.append(np.array(frame))

        # Calculate the number of frames to keep for each second
        num_frames = len(frames)
        frames_to_keep = int(num_frames / slowdown_percentage)

        new_frames = []
        step = num_frames // frames_to_keep
        for i in range(0, num_frames, step):
            new_frames.append(frames[i])

        # Save the new video as an image sequence (for simplicity)
        output_prefix = 'slowdown_frame_'
        for idx, frame in enumerate(new_frames):
            Image.fromarray(frame).save(f"{output_prefix}{idx:04d}.png")

        print("Video successfully slowed down and saved as image sequence.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
