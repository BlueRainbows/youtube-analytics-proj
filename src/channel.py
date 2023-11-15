import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = 'AIzaSyAvSJwZZPDCUm5njvSBpnx-41ubiskiQXg'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.service = self.get_service()
        self.youtube_data = self.youtube_file()
        self.title = self.youtube_data['snippet']['title']
        self.description = self.youtube_data['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.youtube_data['snippet']['customUrl']
        self.view_count = self.youtube_data['statistics']['viewCount']
        self.video_count = self.youtube_data['statistics']['videoCount']
        self.subscriber_count = self.youtube_data['statistics']['subscriberCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        def printj(dict_to_print: dict) -> None:
            """ Выводит словарь в json-подобном удобном формате с отступами """
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

        channels_id = self.__channel_id
        channel = self.youtube.channels().list(id=channels_id, part='snippet,statistics').execute()
        printj(channel)

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, name):
        with open(name, 'w'):
            json_file = json.dumps({
                'channel_id': self.__channel_id,
                'title': self.title,
                'description': self.description,
                'custom_url': self.url,
                'subscriber_count': self.subscriber_count,
                'video_count': self.video_count,
                'view_count': self.view_count
            })
        return json_file

    def youtube_file(self):
        channels_id = self.__channel_id
        channel = Channel.get_service().channels().list(id=channels_id, part='snippet,statistics').execute()
        return channel['items'][0]

    def __str__(self):
        return f'{self.title}: {self.url}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)
