from __future__ import annotations

from typing import Mapping

import services
from models.geolocation import Geolocation

CACHE: dict[str, Geolocation] = {}


def fetch_country_from_headers(headers: Mapping[str, str]) -> str:
    if country := headers.get("CF-IPCountry"):
        return country

    if not (ip := headers.get("CF-Connecting-IP")):
        forwards = headers["X-Forwarded-For"].split(",")

        if len(forwards) != 1:
            ip = forwards[0]
        else:
            ip = headers["X-Real-IP"]

    if geolocation := CACHE.get(ip):
        return geolocation.iso_code

    city = services.geolocation.city(ip)

    assert city.country.iso_code is not None
    assert city.location.longitude is not None
    assert city.location.latitude is not None

    iso_code = city.country.iso_code.lower()
    geolocation = Geolocation(
        longitude=city.location.longitude,
        latitude=city.location.latitude,
        iso_code=iso_code,
    )
    CACHE[ip] = geolocation

    return geolocation.iso_code
