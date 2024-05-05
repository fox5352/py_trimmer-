from moviepy.editor import VideoFileClip

import argparse
import re

def trim_video(video_path, start_min, start_sec, end_min, end_sec):
    """
    Trims a video based on the given start and end times in minutes and seconds.
    
    Args:
        video_path (str): The path to the input video file.
        start_min (int): The start minute of the desired clip.
        start_sec (int): The start second of the desired clip.
        end_min (int): The end minute of the desired clip.
        end_sec (int): The end second of the desired clip.
        
    Returns:
        VideoFileClip: The trimmed video clip.
    """

    # Load the video
    video = VideoFileClip(video_path)

    # set the timestamps
    start_time = start_min * 60 + start_sec
    end_time = end_min * 60 + end_sec

    # Trim the video
    trimmed_video = video.subclip(start_time, end_time)
    
    pattern = r'[/\\]([^/\\]+)$'

    match = re.search(pattern, video_path)
    if match:
      directory_path = video_path[:match.start()]
      file_name = match.group(1)

      trimmed_video.write_videofile(f"{directory_path}/trimmed-{file_name}")


def main():
  parser = argparse.ArgumentParser(description="trim videos")
  parser.add_argument('-f', '--file', type=str, required=True, help='Path to the video file')
  parser.add_argument('-m', '--minutes', type=str, help='Start and end minutes in the format "start_min:end_min"')
  parser.add_argument('-s', '--seconds', type=str, help='Start and end seconds in the format "start_sec:end_sec"')

  args = parser.parse_args()

  file_path = args.file

  if args.minutes and args.seconds:
    
    start_min, end_min = map(int, args.minutes.split(':'))
    start_sec, end_sec = map(int, args.seconds.split(':'))

    trim_video(video_path=file_path, start_min=start_min, start_sec=start_sec, end_min=end_min, end_sec=end_sec)

  else:
    print("Please provide start and end minutes and seconds in the format \"start_min:end_min\" and \"start_sec:end_sec\"")
    exit(1)

if __name__ == "__main__":
  main()
