from typing import Mapping
from typing import TypedDict

from app.common.context import Context


def retrieve_ip_from_headers(headers: Mapping[str, str]) -> str | None:
    # try cloudflare first
    cloudflare_ip = headers.get("CF-Connecting-IP")
    if cloudflare_ip is not None:
        return cloudflare_ip

    # next, try forwards
    forwards_str = headers.get("X-Forwarded-For")
    if forwards_str is not None:
        forwards = forwards_str.split(",")
        if len(forwards) != 1:
            return forwards[0]

    # lastly, try real ip
    real_ip = headers.get("X-Real-IP")
    if not real_ip:
        return None

    return real_ip


class Geolocation(TypedDict):
    latitude: float
    longitude: float
    country_acronym: str


def fetch_geolocation_from_ip(ctx: Context, ip: str) -> Geolocation:
    result = ctx.geolocation_reader.city(ip)

    if result.country.iso_code is not None:
        acronym = result.country.iso_code.lower()
    else:
        acronym = "xx"

    return {
        "latitude": result.location.latitude or 0.0,
        "longitude": result.location.longitude or 0.0,
        "country_acronym": acronym,
    }
