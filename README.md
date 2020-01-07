# youtube-dl scripts
These are the scripts which I use to download youtube videos on Windows. The youtube-dl scripts themselves are based off of https://www.reddit.com/r/DataHoarder/comments/c6fh4x/after_hoarding_over_50k_youtube_videos_here_is/. There is little deviation in my scripts from his so this is mostly so I don't lose them. I encourage that if you want to make your own scripts to use his post as a starting point. On Windows you will need both youtube-dl.exe and ffmpeg.exe in the root directory. They are separated into two directories for either Windows or Linux. I recently switched to Linux so that will be the most updated.

# updateArchive.py
This script a command line tool to generate new and backup old archive.log files which are created using youtube-dl and are based on your current directory. I wrote it using python3 and it works for both Windows and Linux. It backs up and then rewrites a new archive.log file in the root directory of your youtube-dl downloads based off of the files which are currently in your directory. This keeps your archive.log up to date with what is actually on your machine incase you deleted or lost any videos. This script does keep a backup of your old archive.log file just incase there is any error which happens you can manually go in and replace it.

This script ONLY works if you use the the naming conventions which u/Veloldo uses in his post (the same conventions I use in my scripts which are based off of his). Always keep a backup of your archive.log file before running this script for the first time even though it does generate one for you. Thanks.

## Usage
`python3 updateArchive.py` - This is the default command, it must be executed in the root directory of your youtube-dl videos and creates a backup folder in that directory.

`python3 updateArchive.py [path of current archive.log]` - You must enter the path of your youtube-dl directory and the script will generate a new archive.log and backup the old logs there. This allows it to be executed anywhere aslong as you include the path.
  
`python3 updateArchive.py [path of current archive.log] [path for backup of old archive.log]` - You must specify the root of your youtube-dl directory and where you would like to back your archive.log file up to. This allows for the backup of the archive.log files to be store in a different directory.
