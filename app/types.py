from typing import NotRequired, Literal, TypedDict
from .enums import ContentType


class Media(TypedDict):
    Poster: str
    Title: str
    Year: str
    Type: ContentType
    imdbID: str

    @classmethod
    def get_columns(cls) -> list[str]:
        return list(
            cls.__annotations__.keys(),
        )


class MediaRequestParams(TypedDict):
    apikey: str
    s: str
    type: NotRequired[ContentType]
    page: int


class MediaResponseData(TypedDict):
    Response: Literal["True", "False"]
    Search: list[Media]
