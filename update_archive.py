#!/usr/bin/python3
import os
import json
from time import time

from ArchiveLog import ArchiveLog


def main():
    start = time()
    root_dir = '/media/miller/Primary/yt-dlp'
    # root_dir = os.getcwd()

    archive = ArchiveLog(os.path.join(root_dir, 'archive.log'))
    archive.get_current_videos()
    archive.backup_existing_archive()  # make this a param on write_new_file
    archive.write_new_file()

    archive.compute_statistics()
    print(json.dumps(archive.stats, indent=2, default=str))
    print(time() - start, 'seconds')


if __name__ == '__main__':
    main()
