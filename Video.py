from string import Template

import requests


class Video:
    status = None
    youtube_id = None
    file_path = None

    def __init__(self, youtube_id, file_path):
        self.youtube_id = youtube_id
        self.file_path = file_path

    def set_status(self) -> None:
        url_template = Template('https://noembed.com/embed?url=https://www.youtube.com/watch?v=$video_id')
        try:
            res = requests.get(
                url=url_template.substitute(video_id=self.youtube_id),
                headers={'User-Agent': 'My User Agent 1.0', }
            )
        except Exception as err:  # todo: refine expected exceptions
            print(err)
        else:
            self.status = res.json().get('error', '200 Success')
            # print(f'{self.status}: {self.youtube_id}')
