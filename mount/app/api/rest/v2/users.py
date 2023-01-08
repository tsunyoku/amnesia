from datetime import datetime
from datetime import timedelta

from app.common.context import Context
from app.models.lazer.dated_count import DatedCount
from app.models.lazer.html_body import HTMLBody
from app.models.lazer.user import User
from app.models.lazer.user_account_history import UserAccountHistory
from app.models.lazer.user_achievement import UserAchievement
from app.models.lazer.user_badge import UserBadge
from app.models.lazer.user_group import UserGroup
from app.models.lazer.user_kudosu import UserKudosu
from app.models.lazer.user_profile_banner import UserProfileBanner
from app.models.lazer.user_profile_page import UserProfilePage
from app.models.lazer.user_rank_highest import UserRankHighest
from app.models.lazer.user_rank_history import UserRankHistory
from app.models.lazer.user_statistics import UserStatistics
from app.models.scope import Scope
from app.models.scope_enforcer import ScopeEnforcer
from app.models.status import Status
from app.models.token import OAuthToken
from app.usecases import groups as groups_usecases
from app.usecases import users as users_usecases
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()


# used to define the exact parameters of the response


class GetUser(User):
    account_history: list[UserAccountHistory]
    active_tournament_banner: UserProfileBanner
    badges: list[UserBadge]
    beatmap_playcounts_count: int
    favourite_beatmapset_count: int
    follower_count: int
    graveyard_beatmapset_count: int
    groups: list[UserGroup]
    loved_beatmapset_count: int
    mapping_follower_count: int
    monthly_playcounts: list[DatedCount]
    page: HTMLBody
    pending_beatmapset_count: int
    previous_usernames: list[str]
    rank_highest: UserRankHighest
    rank_history: UserRankHistory
    ranked_beatmapset_count: int
    replays_watched_counts: list[DatedCount]
    scores_best_count: int
    scores_first_count: int
    scores_recent_count: int
    statistics: UserStatistics
    support_level: int
    user_achievements: list[UserAchievement]


class OwnUser(GetUser):
    statistics_rulesets: dict[str, UserStatistics]
    is_restricted: bool


@router.get("/api/v2/me", response_model=OwnUser)
async def fetch_self(
    ctx: Context = Depends(),
    oauth_token: OAuthToken = Depends(ScopeEnforcer(Scope.IDENTIFY)),
) -> OwnUser:
    user = await users_usecases.fetch_one(
        ctx,
        id=oauth_token.user_id,
        status=None,
    )
    assert user is not None

    user.last_visit

    group = await groups_usecases.fetch_one(ctx, id=user.default_group)
    assert group is not None

    user = OwnUser(
        avatar_url=f"https://a.akatsuki.pw/{user.id}",
        country_code=user.country_acronym,
        default_group=group.name,
        id=user.id,
        is_active=user.last_visit > (datetime.now() - timedelta(weeks=3 * 4)),
        is_bot=False,  # TODO
        is_deleted=user.status is Status.DELETED,
        is_online=False,  # TODO
        is_supporter=user.supporter_until > datetime.now()
        if user.supporter_until
        else False,  # TODO: replace with privilege check
        last_visit=user.last_visit,
        pm_friends_only=user.friend_only_dms,
        profile_colour=None,  # TODO
        username=user.username,
        account_history=[],  # TODO
        active_tournament_banner=None,  # TODO
        badges=[],  # TODO
        beatmap_playcounts_count=0,  # TODO
        blocks=None,  # TODO
        country=None,
        cover=None,  # TODO
        favourite_beatmapset_count=0,  # TODO
        follower_count=0,  # TODO
        friends=None,  # TODO
        graveyard_beatmapset_count=0,  # TODO
        groups=[],  # TODO
        is_restricted=False,  # TODO
        loved_beatmapset_count=0,  # TODO
        mapping_follower_count=0,  # TODO
        monthly_playcounts=[],  # TODO
        page=None,  # TODO
        pending_beatmapset_count=0,  # TODO
        previous_usernames=[],  # TODO
        rank_highest=None,  # TODO
        rank_history=None,  # TODO
        ranked_beatmapset_count=0,  # TODO
        replays_watched_counts=[],  # TODO
        scores_best_count=0,  # TODO
        scores_first_count=0,  # TODO
        scores_recent_count=0,  # TODO
        statistics=None,  # TODO
        statistics_rulesets=None,  # TODO
        support_level=1
        if user.supporter_until is not None and user.supporter_until > datetime.now()
        else 0,  # TODO
        unread_pm_count=None,  # TODO
        user_achievements=[],  # TODO
        user_preferences=None,  # TODO
        cover_url=None,  # TODO
        discord=None,  # TODO
        has_supported=user.supporter_until.timestamp() > 0
        if user.supporter_until
        else False,  # TODO
        interests=None,  # TODO
        join_date=user.created_at,
        kudosu=UserKudosu(total=0, available=0),  # TODO
        location=None,  # TODO
        max_blocks=0,  # TODO
        max_friends=0,  # TODO
        occupation=None,  # TODO
        playmode="osu",  # TODO
        playstyle=[],  # TODO
        post_count=0,  # TODO
        profile_order=[
            UserProfilePage.ME,
            UserProfilePage.RECENT_ACTIVITY,
            UserProfilePage.TOP_RANKS,
            UserProfilePage.MEDALS,
            UserProfilePage.HISTORICAL,
            UserProfilePage.BEATMAPS,
            UserProfilePage.KUDOSU,
        ],  # TODO
        title=None,  # TODO
        title_url=None,  # TODO
        twitter=None,  # TODO
        website=None,  # TODO
    )
    return user
