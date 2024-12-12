from pprint import pprint
import requests
from requests.exceptions import HTTPError
from config import DISCORD_TOKEN, DISCORD_BASE_URL


class ApiClient:
    def __init__(self, token: str = DISCORD_TOKEN) -> None:
        self.token = token
        self.base_url = DISCORD_BASE_URL
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Discogs token={self.token}",
                "User-Agent": "meloman/1.0",
            }
        )

    def get(
        self, endpoint, params: dict = None, payload: dict = None
    ) -> requests.Session:
        try:
            response = self.session.get(
                url=self.base_url + endpoint, params=params, json=payload
            )
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            print(f"HTTP Error: {e}")
            return {"error": str(e)}
