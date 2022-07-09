# youtube-dl scripts
These are the scripts which I use to download youtube videos. The youtube-dl scripts themselves are based off of https://www.reddit.com/r/DataHoarder/comments/c6fh4x/after_hoarding_over_50k_youtube_videos_here_is/. There is little deviation in my scripts so this repo is primarily so I don't lose them. Feel free to use this as a starting point.

# updateArchive.py
This script a command line tool to generate new and backup old archive.log files which are created using youtube-dl and are based on your current directory. I wrote it using python3 and has been tested with Linux only. It backs up and then writes a new archive.log file in the root directory of your directory based off of the videos/files which are currently in your directory. This keeps your archive.log up to date with what is actually on your machine. Use case being if you deleted or lost any videos. The script keeps a backup of your old archive.log file just incase there is any error which happens you can manually go in and replace it.

This script ONLY works if you use the the naming conventions which u/Veloldo uses in his post (the same conventions I use in my scripts which are based off of his). Always keep a backup of your archive.log file before running this script for the first time even though it does generate one for you. Thanks.

## Usage
`python3 update-archive.py` - This is the default command, it must be executed in the root directory of your youtube-dl videos and creates a backup folder in that directory.
