import json
from googleapiclient.discovery import build


class Channel:
    api_key: str = 'AIzaSyAvSJwZZPDCUm5njvSBpnx-41ubiskiQXg'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_channel):
        self.id_channel = id_channel

    def print_info(self):
        """ Принимает данные о id канала и выводит информацию о нём"""

        def printj(dict_to_print: dict) -> None:
            """ Выводит словарь в json-подобном удобном формате с отступами """
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

        channel_id = self.id_channel
        channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)

