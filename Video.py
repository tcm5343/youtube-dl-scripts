from os import PathLike
from string import Template
from typing import Optional, Union

import requests


class Video:
    _noembed_template = Template('https://noembed.com/embed?url=https://www.youtube.com/watch?v=$video_id')

    status: Optional[str]
    """
    Status definitions:
    200 Success: The video exists and is accessible
    400 Bad Request: The video never existed, url is bad
    401 Unauthorized: The video is not embeddable (however, the video is accessible)
    403 Forbidden: The video has been made private
    404 Not Found: The video has been deleted
    """
    youtube_id: str
    file_path: Union[str, PathLike]
    noembed_url: str

    def __init__(self, youtube_id: str, file_path: Union[str, PathLike]):
        self.youtube_id = youtube_id
        self.file_path = file_path
        self.noembed_url = self._noembed_template.substitute(video_id=youtube_id)
        self.status = None

    def fetch_status(self) -> str:
        """
        Sends a request to noembed.com to determine current status of the video.
        :return: Video status
        """
        try:
            res = requests.get(
                url=self._noembed_template.substitute(video_id=self.youtube_id),
                headers={'User-Agent': 'My User Agent 1.0', }
            )
        except Exception as err:  # todo: refine error handling
            print(err)
            res = requests.get(
                url=self._noembed_template.substitute(video_id=self.youtube_id),
                headers={'User-Agent': 'My User Agent 1.0', }
            )

        self.status = res.json().get('error', '200 Success')
        return self.status
