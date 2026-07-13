#  convert the mp4 to mp3 using ffmpeg
import os
import subprocess

files=os.listdir("video")
print (files)
for file in files:
    #print(file)
    tutorial_number=file.split(" [")[0].split(" #")[1]
    #print (tutorial_number)
    file_name=file.split(" ｜ ")[0]
    print (tutorial_number,file_name)
    subprocess.run(["ffmpeg","-i",f"video/{file}",f"voice/{tutorial_number}_{file_name}.mp3"])