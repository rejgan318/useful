import configparser

from get_video_name import get_video_names


config = configparser.ConfigParser()
config.read('config.ini')

video_files = get_video_names(config)

print("Done.")
