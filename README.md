# youtube-dl scripts
These are the scripts which I use to download youtube videos. The youtube-dl scripts themselves are based off of https://www.reddit.com/r/DataHoarder/comments/c6fh4x/after_hoarding_over_50k_youtube_videos_here_is/. There is little deviation in my scripts from his so this is mostly so I don't lose them. I encourage that if you want to make your own scripts to use his post as a starting point.

# updateArchive
This script I wrote using python3 and is meant to be executed in the root of your youtube-dl directory. It deletes and rewrites a new archive.log file in your root directory based off of the files which are currently on your machine. This keeps your archive.log up to date with what is actually on your machine incase you deleted any videos.

This script ONLY works if you use the the naming conventions which u/Veloldo uses in his post (the same conventions I use in my scripts which are based off of his).
