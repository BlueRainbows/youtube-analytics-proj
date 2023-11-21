from googleapiclient.discovery import build


class Video:
    api_key: str = 'AIzaSyAvSJwZZPDCUm5njvSBpnx-41ubiskiQXg'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.id_video = id_video
        self.video_title = self.get_info_video()[0]
        self.video_url = 'https://www.youtube.com/watch?v=' + self.id_video
        self.view_count = self.get_info_video()[1]
        self.like_count = self.get_info_video()[2]

    def get_info_video(self):
        list_value = []
        video_id = self.id_video
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        video_title: str = video_response['items'][0]['snippet']['title']
        list_value.append(video_title)
        view_count: int = video_response['items'][0]['statistics']['viewCount']
        list_value.append(view_count)
        like_count: int = video_response['items'][0]['statistics']['likeCount']
        list_value.append(like_count)
        return list_value

    def __str__(self):
        return self.video_title


class PLVideo(Video):

    def __init__(self, id_video, playlist_id):
        super().__init__(id_video)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.video_title
