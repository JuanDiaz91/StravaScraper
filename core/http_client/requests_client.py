import requests
from browserforge.headers import HeaderGenerator


class RequestsClient:
    def __init__(self):
        self.session = requests.Session()
        self.headers = self._get_custom_headers()

    def load_cookies(self, cookies: dict):
        self.session.cookies.update(cookies)

    def _get_custom_headers(self) -> dict:
        return HeaderGenerator(
            browser='chrome',
            os='windows',
            device='desktop',
            locale='es-ES',
            http_version=2
        ).generate()

    def request_get(self, url: str, params: str=None) -> requests.Response:
        return self.session.get(url, headers=self.headers, params=params)

    def request_post(self, url: str, json: dict=None, data: dict=None) -> requests.Response:
        return self.session.post(url, headers=self.headers, json=json, data=data)
