from requests import RequestException
import math
import requests

from .enums import ContentType
from .types import *


MAX_MEDIA_PER_GET = 8


def get_media(
    url: str,
    api_key: str,
    title: str,
    content_type: ContentType,
    limit: int,
) -> list[Media]:

    def create_params(page: int) -> MediaRequestParams:
        params = {"apikey": api_key, "s": title, "page": page}
        if content_type != ContentType.ALL:
            params["type"] = content_type
        return params

    def fetch_data(params: MediaRequestParams) -> MediaResponseData:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def extract_media(data: MediaResponseData) -> list[Media]:
        media = data.get("Search", [])
        not_found = data.get("Response") != "True" or media == []
        if not_found:
            raise LookupError()
        return media

    def sort(media: list[Media]) -> list[Media]:
        return sorted(
            media,
            key=lambda m: (m["Title"], m["Year"]),
        )

    total_pages = math.ceil(limit / MAX_MEDIA_PER_GET)
    media = []

    for page in range(1, total_pages + 1):
        params = create_params(page)
        try:
            data = fetch_data(params)
            media.extend(
                extract_media(data),
            )
        except (RequestException, LookupError):
            break

    return sort(media[:limit])
