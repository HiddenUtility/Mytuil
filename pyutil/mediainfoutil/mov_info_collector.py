

from pymediainfo import MediaInfo

class MovFileInformationCollector:
    def __init__(self):
        ...

    def get_creation_date_pymediainfo(file_path) -> str:
        media_info = MediaInfo.parse(file_path)
        for track in media_info.tracks:

            if track.track_type == "Audio":
                # pprint(track.to_data())
                data = track.to_data()
                tagged = data.get('tagged_date')
                return tagged