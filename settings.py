import logging
from decouple import config

from core.file_system.file_system_manager import FileSystemManager


#### COOKIES ####
STRAVA4_SESSION = config('STRAVA_SESSION')
STRAVA_REMEMBER_ID = config('STRAVA_REMEMBER_ID')
STRAVA_REMEMBER_TOKEN = config('STRAVA_REMEMBER_TOKEN')


COOKIES_SESSION = {
    '_strava4_session': STRAVA4_SESSION,
    'strava_remember_id': STRAVA_REMEMBER_ID,
    'strava_remember_token': STRAVA_REMEMBER_TOKEN,
}


#### FastApi Config ####
UVICORN_HOST = config('UVICORN_HOST')
UVICORN_PORT = int(config('UVICORN_PORT'))

BASE_URL = "https://www.strava.com"


### ROUTES ####
fs_manager = FileSystemManager()

def project_setup():
    fs_manager.ensure_directories()

### Basic Logger ###
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)
