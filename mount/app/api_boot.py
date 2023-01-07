from app.api import init_api
from app.common import logger
from app.common import settings

logger.init_logging(settings.LOG_LEVEL)

api = init_api()
