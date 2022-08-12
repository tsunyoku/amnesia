from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel

from .account_history import UserAccountHistory
from .profile_banner import ProfileBanner
from .user_badge import UserBadge
from models.osu.user_group import UserGroup
from models.osu.user_monthly_playcount import UserMonthlyPlaycount


class UserCompact(BaseModel):
    id: int
    username: str
    profile_colour: str | None
    avatar_url: str
    country_code: str
    is_active: bool
    is_bot: bool
    is_deleted: bool
    is_online: bool
    is_supporter: bool
    last_visit: datetime | None
    pm_friends_only: bool

    # optional attributes (per endpoint)
    # NOTE: some types are guesses since documentation don't have them all listed
    account_history: list[UserAccountHistory] | None
    active_tournament_banner: ProfileBanner | None
    badges: list[UserBadge] | None
    beatmap_playcounts_count: int | None
    pending_beatmapset_count: int | None
    friends: list[int] | None
    page: int | None
    cover: str | None
    previous_usernames: list[str] | None
    ranked_beatmapset_count: int | None
    scores_best_count: int | None
    scores_first_count: int | None
    scores_recent_count: int | None
    unread_pm_count: int | None
    favourite_beatmapset_count: int | None
    follower_count: int | None
    graveyard_beatmapset_count: int | None
    groups: list[UserGroup] | None
    is_restricted: bool | None
    loved_beatmapset_count: int | None
    monthly_playcounts: list[UserMonthlyPlaycount] | None

    # TODO: work out what types these are cus documentation don't have them listed
    blocks: Any
    country: Any
    rank_history: Any
    replays_watched_counts: Any
    statistics: Any
    statistics_rulesets: Any  # UserStatisticsRulesets ?
    support_level: Any
    user_achievements: Any
    user_preferences: Any
