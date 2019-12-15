import os

# this script generates a new and up to date archive.log for your downloaded youtube videos
# author: @tcm5343

# finds working directory
rootdir = os.getcwd()

# creates archive file
f = open("archive.log", "w")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".mkv") or filepath.endswith(".webm"):
             # returns index of the last space before the url hash
             index = file.rfind(" ")
             f.write("youtube ")
             # returns url hash and gets rid of file extension
             f.write((file[index+1:]).split(".",1)[0] +"\n")
f.close()
