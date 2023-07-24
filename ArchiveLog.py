from typing import Dict, Union
import os
import shutil

import grequests

from Video import Video

EXT_TO_ARCHIVE = ('.m4a', '.mp3', '.mp4', '.wav', '.webm', '.mkv')


class ArchiveLog:
    videos: Dict[str, Union[Video, int]]
    archive_file_path: Union[str, os.PathLike]
    backup_dir_path: Union[str, os.PathLike]
    yt_dlp_root_dir_path: Union[str, os.PathLike]
    stats: dict

    def __init__(self, archive_file_path: str):
        self.archive_file_path = archive_file_path
        self.yt_dlp_root_dir_path = os.path.dirname(archive_file_path)
        self.backup_dir_path = self.yt_dlp_root_dir_path + '/archive_log_backups'
        self.videos = {}

    def get_current_videos(self):
        for subdir, dirs, files in os.walk(self.yt_dlp_root_dir_path):
            for file in files:
                filepath = os.path.join(subdir, file)
                # print(filepath)
                video_id = file[file.rfind(' ') + 1:].split('.', 1)[0]
                if os.path.splitext(filepath)[1] in EXT_TO_ARCHIVE:
                    if self.videos.get(video_id):
                        # print(video_id, 'is a duplicate')
                        ...
                    else:
                        self.videos[video_id] = Video(youtube_id=video_id, file_path=filepath)

    def backup_existing_archive(self) -> None:
        if os.path.exists(self.archive_file_path):
            if not os.path.exists(self.backup_dir_path):
                os.makedirs(self.backup_dir_path)
            backup_archive_count = len([name for name in os.listdir(self.backup_dir_path)]) + 1
            backup_path = os.path.join(self.backup_dir_path, f'archive_{backup_archive_count}.log')
            shutil.copy2(self.archive_file_path, backup_path)

    def write_new_file(self, file_path=None, backup_existing: bool = False):
        if backup_existing:
            self.backup_existing_archive()
        file_path = file_path if file_path else self.archive_file_path
        with open(file_path, 'w') as archive_file:
            archive_file.writelines([f'youtube {video.youtube_id}\n' for video in self.videos.values()])

    def add_video(self, video: Video) -> None:
        self.videos[video.youtube_id] = video

    def exception(self, request, exception):
        # print("Problem: {}: {}".format(request.url, exception))
        ...

    def compute_statistics(self) -> Dict[str, Union[Video, int]]:
        self.stats = {
            'Total Count': 0
        }

        results = grequests.map(
            (grequests.get(video.noembed_url) for video in self.videos.values() if isinstance(video, Video)),
            exception_handler=self.exception,
            size=60
        )

        for res in results:  # todo: handle if res is None
            self.stats['Total Count'] += 1

            video_url = res.json()['url']
            video_id = video_url[video_url.find('watch?v=') + len('watch?v='):]
            video_status = res.json().get('error', '200 Success')
            self.videos[video_id].status = video_status

            if self.stats.get(video_status):
                if video_status != '200 success':
                    self.stats[video_status].append(self.videos[video_id].youtube_id)
                self.stats[f'{video_status} Count'] += 1
            else:
                if video_status != '200 success':
                    self.stats[video_status] = [self.videos[video_id].youtube_id]
                self.stats[f'{video_status} Count'] = 1

        return self.stats

    # def compute_statistics(self) -> Dict[str, Union[Video, int]]:
    #     self.stats = {
    #         'Total Count': 0
    #     }
    #
    #     for video in self.videos.values():
    #         self.stats['Total Count'] += 1
    #         video.fetch_status()
    #         if self.stats.get(video.status):
    #             if video.status != '200 success':
    #                 self.stats[video.status].append(video.youtube_id)
    #             self.stats[f'{video.status} Count'] += 1
    #         else:
    #             if video.status != '200 success':
    #                 self.stats[video.status] = [video.youtube_id]
    #             self.stats[video.status] = [video.youtube_id]
    #             self.stats[f'{video.status} Count'] = 1
    #
    #     return self.stats
