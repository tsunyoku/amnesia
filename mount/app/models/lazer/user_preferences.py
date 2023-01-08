from enum import Enum

from app.models import BaseModel


class UserBeatmapsetDownload(str, Enum):
    ALL = "all"
    NO_VIDEO = "no_video"
    DIRECT = "direct"


class UserListFilter(str, Enum):
    ALL = "all"
    ONLINE = "online"
    OFFLINE = "offline"


class UserListSort(str, Enum):
    LAST_VISIT = "last_visit"
    RANK = "rank"
    USERNAME = "username"


class UserListView(str, Enum):
    CARD = "card"
    LIST = "list"
    BRICK = "brick"


class UserPreferences(BaseModel):
    audio_autoplay: bool | None
    audio_muted: bool | None
    audio_volume: int | None
    beatmapset_download: UserBeatmapsetDownload | None
    beatmapset_show_nsfw: bool | None
    beatmapset_title_show_original: bool | None
    comments_show_deleted: bool | None
    forum_posts_show_deleted: bool
    ranking_expanded: bool | None
    user_list_filter: UserListFilter | None
    user_list_sort: UserListSort | None
    user_list_view: UserListView | None
