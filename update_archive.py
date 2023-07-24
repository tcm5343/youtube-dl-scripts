# from time import time
# import json
import os

from ArchiveLog import ArchiveLog


def main():
    # root_dir = '/media/miller/Primary/yt-dlp'
    root_dir = os.getcwd()

    archive = ArchiveLog(os.path.join(root_dir, 'archive.log'))
    archive.get_current_videos()
    archive.write_new_file(backup_existing=True)

    # archive.compute_statistics()
    # print(json.dumps(archive.stats, indent=2, default=str))


if __name__ == '__main__':
    main()
