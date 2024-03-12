from httputil.HttpConfiguration import HttpConfiguration

import requests


class HttpClient:
    HOST : str = HttpConfiguration.HOST.value
    PORT : int = HttpConfiguration.PORT.value

    def __init__(self) -> None:
        pass

    def send_request(self):
        response = requests.get(f'http://{self.HOST}:{self.PORT}')
        print(f'Response from server: {response.text}')

