#!/usr/bin/python3

# a command line tool to generate new and backup old archive.log files which are created using youtube-dl

import os
import shutil

EXT_TO_ARCHIVE = ('.m4a', '.mp3', '.mp4', '.wav', '.webm', '.mkv')

# ROOT_DIR = '/media/miller/Primary/yt-dlp'
ROOT_DIR = os.getcwd()
BACKUP_DIR = ROOT_DIR + '/archive_backups'


def archive_existing_log_file() -> None:
    source_path = os.path.join(ROOT_DIR, 'archive.log')
    if os.path.exists(source_path):
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        backup_archive_count = len([name for name in os.listdir(BACKUP_DIR)]) + 1
        backup_path = os.path.join(BACKUP_DIR, f'archive{backup_archive_count}.log')
        
        shutil.copy2(source_path, backup_path)


def create_log_file() -> None:
    with open(os.path.join(ROOT_DIR, 'archive.log'), 'w') as archive_file:
        for subdir, dirs, files in os.walk(ROOT_DIR):
            for file in files:
                filepath = os.path.join(subdir, file)
                if os.path.splitext(filepath)[1] in EXT_TO_ARCHIVE:
                    video_url_hash = file[file.rfind(' ') + 1:].split('.', 1)[0]
                    archive_file.write(f'youtube {video_url_hash}\n')


def display_results():
    with open(os.path.join(ROOT_DIR, 'archive.log'), 'r') as archive_file:
        print('Total Videos Archived: \t' + str(sum(1 for _ in archive_file)))


def main():
    archive_existing_log_file()
    create_log_file()
    display_results()


if __name__ == '__main__':
    main()
