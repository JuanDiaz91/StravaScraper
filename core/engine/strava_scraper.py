from core.file_system.file_system_manager import FileSystemManager
from extract_data import extract_user_profile, extract_pagination_user_list, extract_users_list
from models import UserProfile
from settings import COOKIES_SESSION, BASE_URL
from core.http_client.requests_client import RequestsClient


class StravaRouteBuilder:
    @classmethod
    def onboarding(cls) -> str:
        return f"{BASE_URL}/onboarding"

    @classmethod
    def user_profile(cls, user_id: int) -> str:
        return f"{BASE_URL}/athletes/{user_id}"

    @classmethod
    def search_users(cls, name: str, page: int = 1) -> str:
        return f"{BASE_URL}/athletes/search?text={name}&page={page}"


class StravaScraper:
    def __init__(self, client_http: RequestsClient):
        self.client = client_http
        self.fs_manager = FileSystemManager()
        self._is_authenticated = self.check_authentication()

    def check_authentication(self) -> bool:
        self.client.load_cookies(cookies=COOKIES_SESSION)
        res = self.client.request_get(url=StravaRouteBuilder.onboarding())

        return True if res.status_code == 200 else False

    def get_profile_by_id(self, user_id: int) -> UserProfile:
        resp = self.client.request_get(url=StravaRouteBuilder.user_profile(user_id=user_id))

        return extract_user_profile(resp_text=resp.text, user_id=user_id)

    def get_profiles_by_ids(self, user_id_list: list[int]) -> list[UserProfile]:
        return [self.get_profile_by_id(user_id=user_id) for user_id in user_id_list]

    def get_users_by_name(self, user_name: str) -> list[UserProfile]:
        all_user = []
        resp = self.client.request_get(url=StravaRouteBuilder.search_users(name=user_name))

        max_pages = extract_pagination_user_list(resp_text=resp.text)
        all_user.extend(extract_users_list(resp.text))

        for page in range(2, max_pages + 1):
            resp = self.client.request_get(StravaRouteBuilder.search_users(name=user_name, page=page))
            all_user.extend(extract_users_list(resp.text))

        return all_user

    def export_users(self, users: list[UserProfile], filename: str = None):
        self.fs_manager.export_to_json([user.to_dict() for user in users], filename=filename)
