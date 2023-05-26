from moviepy.editor import *
import os

YT_PATH = "./yt_downloads/"
MP3_PATH = "./mp3_versions/"

def mp4tomp3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

# -------------
if __name__ == '__main__':

    listed = os.listdir(YT_PATH)
    for elem in listed:
        filename = elem.split(".")[0]
        mp4tomp3(YT_PATH+filename+".mp4", MP3_PATH+filename+".mp3")
        print(f"File named {filename} is converted to mp3.")
    print("All task completed.")
