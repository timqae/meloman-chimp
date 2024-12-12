from pprint import pprint
import random
import requests
from  discogs_services.api_client import ApiClient
from utils.msg_formatters import format_album_message


class Search:
    """
    Issue a search query to our database. This endpoint accepts pagination parameters.
    https://www.discogs.com/developers/#page:database,header:database-search
    """

    def __init__(self, client: ApiClient):
        self.client = client

    def search(self, query: str = None, **kwargs) -> requests.Session:
        """Issue a search query
        Parameters
            query (str, optional): Your search query; defaults to None
            type (str, optional): Example: release; defaults to None
            title (str, optional): Search by combined “Artist Name - Release Title” title field; defaults to None
            release_title (str, optional): Search release titles; defaults to None
            credit (str, optional): Search release credits; defaults to None
            artist (str, optional): Search artist names; defaults to None
            Anv (str, optional): Search artist ANV; defaults to None
            label (str, optional): Search label names; defaults to None
            genre (str, optional): Search genres; defaults to None
            style (str, optional): Search styles; defaults to None
            country (str, optional): Search release country; defaults to None
            year (str, optional): Search release year; defaults to None
            format (str, optional): Search formats; defaults to None
            catno (str, optional): Search catalog number; defaults to None
            barcode (str, optional): Search barcodes; defaults to None
            track (str, optional): Search track titles; defaults to None
            submitter (str, optional): Search submitter username; defaults to None
            contributor (str, optional): Search contributor usernames; defaults to None

        Returns:
            requests.Session: The response from the Discogs API
        """
        end_point = "/database/search"

        params = {"q": query, **kwargs}

        response = self.client.get(end_point, params=params)

        if "error" in response:
            return response

        results = response.get("results", [])
        pagination = response.get("pagination", [])

        return results, pagination

    def random_album_choise(self, genre: dict):

        predefined = {
            "media_format": "album",
        }
        predefined.update(genre)
        pprint(f"[random choice predefined -> ] \n{predefined}")

        result = self.search(predefined)[0]
        choice = random.choice(result)
        # pprint(f"[random choice -> ]\n")
        # pprint(choice)

        title = choice.get("title", None)
        style = choice.get("style", None)
        country = choice.get("country", None)
        year = choice.get("year", None)
        genre = choice.get("genre", None)
        uri = choice.get("uri", None)
        url = f"https://www.discogs.com{uri}"

        return format_album_message(title, genre, style, country, year, url)


if __name__ == "__main__":
    client = ApiClient()

    search = Search(client)
    callback_data_storage = {}

    chat_id = "chat1"
    callback_data = "Rock"

    # if chat_id not in callback_data_storage:
    #     callback_data_storage[chat_id] = {}

    # callback_data_storage[chat_id]["genre"] = callback_data
    # pars = callback_data_storage[chat_id]

    search.random_album_choise({"genre": "Rock"})

    # predefined = {
    #     "q": query,
    #     "type": type,
    #     "title": title,
    #     "release_title": release_title,
    #     "credit": credit,
    #     "artist": artist,
    #     "anv": Anv,
    #     "label": label,
    #     "genre": genre,
    #     "style": style,
    #     "country": country,
    #     "year": year,
    #     "format": format,
    #     "catno": catno,
    #     "barcode": barcode,
    #     "track": track,
    #     "submitter": submitter,
    #     "contributor": contributor,
    # }
