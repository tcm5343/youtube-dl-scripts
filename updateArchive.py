#!/usr/bin/python3

import os, shutil, sys, getopt

# a command line tool to generate new and backup old archive.log files which are created using youtube-dl and are based on your current directory
# author: @tcm5343

# function archives the current archive.log file in the directory
def archiveCurrentLog():
    if os.path.exists(rootdir + "/archive.log"):
        # archives existing archive.log file (one is made d)
        if not os.path.exists(backupdir):
            os.makedirs(backupdir)

        # finds the number of archived logs currently in the backup directory
        archiveCount = len([name for name in os.listdir(backupdir)]) + 1
        
        # copies current archive.log into new directory
        source = rootdir + "/archive.log"
        destination = backupdir +"/archive" + str(archiveCount) + ".log"
        dest = shutil.copy2(source, destination)

# function populates a new archive.log based on videos in the directory
def populateNewLog():
    f = open("archive.log", "w")
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if os.path.splitext(filepath)[1].endswith(tuple(ext)):
                 # returns index of the last space before the url hash
                 index = file.rfind(" ")
                 f.write("youtube ")
                 # returns url hash and gets rid of file extension
                 f.write((file[index+1:]).split(".",1)[0] +"\n")
    f.close()

def displayResults():
    print(sys.argv[0] + " is finished:")
    with open('archive.log') as my_file:
        print("Total Videos: \t" + str(sum(1 for _ in my_file)))

# variable declaration
ext = (".3gp" or ".aac" or ".flv" or ".m4a" or ".mp3" or ".mp4" or ".ogg" or ".wav" or ".webm")
rootdir = "";
backupdir = "";

# default directories
if len(sys.argv) == 1:
    rootdir = os.getcwd()
    backupdir = rootdir + "/backupOfArchiveLogs"
    archiveCurrentLog()
    populateNewLog()
    displayResults()

elif len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
    rootdir = sys.argv[1]
    backupdir = sys.argv[1] + "/backupOfArchiveLogs"
    archiveCurrentLog()
    populateNewLog()
    displayResults()
    sys.exit()

elif len(sys.argv) == 2 and sys.argv[1] == "--help":
    # usage of this script
    print("\n" + sys.argv[0] + " is a command line tool to generate new and backup old archive.log files which are created using youtube-dl and are based on your current directory.\n")
    print("Usage:")
    print("\tpython3 updateArchive.py\n\t\t- This is the default command, it must be executed in the root directory of your youtube-dl videos and creates a backup folder in that directory.")
    print("\tpython3 updateArchive.py [path of current archive.log]\n\t\t- You must enter the path of your youtube-dl directory and the script will generate a new archive.log and backup the old logs there. This allows it to be executed anywhere aslong as you include the path.")
    print("\tpython3 updateArchive.py [path of current archive.log] [path for backup of old archive.log]\n\t\t- You must specify the root of your youtube-dl directory and where you would like to back your archive.log file up to. This allows for the backup of the archive.log files to be store in a different directory.")
    sys.exit()

# custom root and backup directories
elif len(sys.argv) == 3:
    if os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
        rootdir = sys.argv[1]
        backupdir = sys.argv[2] + "/backupOfArchiveLogs"
        archiveCurrentLog()
        populateNewLog()
        displayResults()
        
    else:
        print("Path is not valid or does not exist, please try again.")

else:
    print("Invalid arguments, see 'updateArchive.py --help'.")
    sys.exit()

