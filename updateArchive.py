import os, shutil
from timeit import Timer


# this script generates a new and up to date archive.log for your currently downloaded youtube videos
# author: @tcm5343

# function archives the current archive.log file in the directory
def archiveCurrentLog(backupDir):
    if os.path.exists(rootdir + "/archive.log"):
        # archives existing archive.log file (one is made d)
        if not os.path.exists(rootdir + backupDir):
            os.makedirs(rootdir + backupDir)

        # finds the number of archived logs currently in the backup directory
        archiveCount = len([name for name in os.listdir('.' + backupDir)]) + 1
        
        # copies current archive.log into new directory
        source = rootdir + "/archive.log"
        destination = rootdir + backupDir +"/archive" + str(archiveCount) + ".log"
 
        dest = shutil.copy2(source, destination)

# function populates a new archive.log based on videos in the directory
def populateNewLog():
    f = open("archive.log", "w")

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
	        # edit possible file types depending on your setup
            if filepath.endswith(".mkv") or filepath.endswith(".webm"):
                 # returns index of the last space before the url hash
                 index = file.rfind(" ")
                 f.write("youtube ")
                 # returns url hash and gets rid of file extension
                 f.write((file[index+1:]).split(".",1)[0] +"\n")
                 videoCount+1
    f.close()

def displayResults(vCount):
    print("updateArchive.py has finished:")
    print("Total Videos: \t" + str(vCount))
    print("Total Time: \t" + str(vCount))


# finds working directory
rootdir = os.getcwd()

backupDirectory = "/backupOfArchiveLogs"
archiveCurrentLog(backupDirectory)

videoCount = 0
populateNewLog()

displayResults(videoCount)


