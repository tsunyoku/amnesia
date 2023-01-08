from datetime import datetime

from app.models import BaseModel
from app.models.lazer.country import Country
from app.models.lazer.dated_count import DatedCount
from app.models.lazer.html_body import HTMLBody
from app.models.lazer.user_account_history import UserAccountHistory
from app.models.lazer.user_achievement import UserAchievement
from app.models.lazer.user_badge import UserBadge
from app.models.lazer.user_group import UserGroup
from app.models.lazer.user_preferences import UserPreferences
from app.models.lazer.user_profile_banner import UserProfileBanner
from app.models.lazer.user_profile_cover import UserProfileCover
from app.models.lazer.user_rank_highest import UserRankHighest
from app.models.lazer.user_rank_history import UserRankHistory
from app.models.lazer.user_relationship import UserRelationship
from app.models.lazer.user_statistics import UserStatistics


class UserCompact(BaseModel):
    avatar_url: str
    country_code: str
    default_group: str
    id: int
    is_active: bool  # active in last 3 minths
    is_bot: bool
    is_deleted: bool
    is_online: bool
    is_supporter: bool
    last_visit: datetime | None  # None if online presence is hidden
    pm_friends_only: bool
    profile_colour: str | None  # hex code
    username: str

    # optional attributes
    account_history: list[UserAccountHistory] | None
    active_tournament_banner: UserProfileBanner | None
    badges: list[UserBadge] | None
    beatmap_playcounts_count: int | None
    blocks: UserRelationship | None
    country: Country | None
    cover: UserProfileCover | None
    favourite_beatmapset_count: int | None
    follower_count: int | None
    friends: list[UserRelationship] | None
    graveyard_beatmapset_count: int | None
    groups: list[UserGroup] | None
    is_restricted: bool | None
    loved_beatmapset_count: int | None
    mapping_follower_count: int | None
    monthly_playcounts: list[DatedCount] | None
    page: HTMLBody | None
    pending_beatmapset_count: int | None
    previous_usernames: list[str] | None
    rank_highest: UserRankHighest | None
    rank_history: UserRankHistory | None
    ranked_beatmapset_count: int | None
    replays_watched_counts: list[DatedCount] | None
    scores_best_count: int | None
    scores_first_count: int | None
    scores_recent_count: int | None
    statistics: UserStatistics | None
    statistics_rulesets: dict[str, UserStatistics] | None
    support_level: int | None
    unread_pm_count: int | None
    user_achievements: list[UserAchievement] | None
    user_preferences: UserPreferences | None
