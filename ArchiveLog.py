from typing import Dict, Union
import os
import shutil

from Video import Video

EXT_TO_ARCHIVE = ('.m4a', '.mp3', '.mp4', '.wav', '.webm', '.mkv')


class ArchiveLog:
    videos: Dict[str, Union[Video, int]] = {}
    archive_file_path = None
    backup_dir_path = None
    yt_dlp_root_dir_path = None
    stats = {None}

    def __init__(self, archive_file_path: str):
        self.archive_file_path = archive_file_path
        self.yt_dlp_root_dir_path = os.path.dirname(archive_file_path)
        self.backup_dir_path = self.yt_dlp_root_dir_path + '/archive_log_backups'

    def get_current_videos(self):
        for subdir, dirs, files in os.walk(self.yt_dlp_root_dir_path):
            for file in files:
                filepath = os.path.join(subdir, file)
                video_id = file[file.rfind(' ') + 1:].split('.', 1)[0]
                if os.path.splitext(filepath)[1] in EXT_TO_ARCHIVE:
                    if self.videos.get(video_id):
                        print(video_id, 'is a duplicate')
                    else:
                        self.videos[video_id] = Video(youtube_id=video_id, file_path=filepath)

    def write_new_file(self, file_path=None):
        file_path = file_path if file_path else self.archive_file_path
        with open(file_path, 'w') as archive_file:
            archive_file.writelines([f'youtube {video.youtube_id}\n' for video in self.videos.values()])

    def backup_existing_archive(self) -> None:
        if os.path.exists(self.archive_file_path):
            if not os.path.exists(self.backup_dir_path):
                os.makedirs(self.backup_dir_path)
            backup_archive_count = len([name for name in os.listdir(self.backup_dir_path)]) + 1
            backup_path = os.path.join(self.backup_dir_path, f'archive_{backup_archive_count}.log')
            shutil.copy2(self.archive_file_path, backup_path)

    def add_video(self, video: Video) -> None:
        self.videos[video.youtube_id] = video

    def compute_statistics(self) -> Dict[str, Union[Video, int]]:
        self.stats = {
            'Total Count': 0
        }

        for video in self.videos.values():
            self.stats['Total Count'] += 1
            video.set_status()
            if self.stats.get(video.status):
                self.stats[video.status].append(video)
                self.stats[f'{video.status} Count'] += 1
            else:
                self.stats[video.status] = [video]
                self.stats[f'{video.status} Count'] = 1

        return self.stats

        # with ThreadPoolExecutor(max_workers=8) as executor:
        #     results = []
        #     for video in tqdm(self.videos.values(), bar_format='{l_bar}{bar:50}{r_bar}{bar:-10b}', dynamic_ncols=True):
        #         results.append(executor.submit(video.set_status))
        #     for result in results:
        #         err = result.exception()
        #         if err:
        #             print(err)
        #
        # # res = [future.result() for future in results]
        # for v in self.videos.values():
        #     print(v.youtube_id, v.status)
        # # print(res)
