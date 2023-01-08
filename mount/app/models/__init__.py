import orjson
import pydantic


class BaseModel(pydantic.BaseModel):
    class Config:
        anystr_strip_whitespace = True
        json_loads = orjson.loads
        json_dumps = orjson.dumps
