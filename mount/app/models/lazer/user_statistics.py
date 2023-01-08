from app.models import BaseModel
from app.models.lazer.user_compact import UserCompact


class UserGradeCounts(BaseModel):
    a: int
    s: int
    sh: int
    ss: int
    ssh: int


class UserLevel(BaseModel):
    current: int
    progress: int


class UserStatistics(BaseModel):
    grade_counts: UserGradeCounts
    hit_accuracy: float
    is_ranked: bool
    level: UserLevel
    maximum_combo: int
    play_count: int
    play_time: int  # TODO: what unit of time is this?
    pp: int
    global_rank: int | None
    ranked_score: int
    replays_watched_by_others: int
    total_hits: int
    total_score: int

    # not always provided, e.g UserCompact references this
    user: UserCompact | None
