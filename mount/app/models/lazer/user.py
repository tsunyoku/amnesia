from datetime import datetime

from app.models.lazer.country import Country
from app.models.lazer.user_compact import UserCompact
from app.models.lazer.user_kudosu import UserKudosu
from app.models.lazer.user_profile_cover import UserProfileCover
from app.models.lazer.user_profile_page import UserProfilePage


class User(UserCompact):
    cover_url: str  # deprecated, remove?
    discord: str | None
    has_supported: bool
    interests: str | None
    join_date: datetime
    kudosu: UserKudosu
    location: str | None
    max_blocks: int
    max_friends: int
    occupation: str | None
    playmode: str
    playstyle: list[str]
    post_count: int
    profile_order: list[UserProfilePage]
    title: str | None
    title_url: str | None
    twitter: str | None
    website: str | None

    # overriding types as always included
    country: Country
    cover: UserProfileCover

    # NOTE: is_restricted will always be given if current authenticated user
