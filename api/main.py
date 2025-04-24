from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from core.engine.strava_scraper import StravaScraper
from core.http_client.requests_client import RequestsClient
from models import UserProfile
from api_models import UserIDList
from settings import UVICORN_HOST, UVICORN_PORT, project_setup, logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Running project setup...")
        project_setup()
        logger.info("Project setup completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during project setup: {e}")
    yield


app = FastAPI(lifespan=lifespan)
scraper = StravaScraper(RequestsClient())


@app.get("/api/profile/{user_id}", response_model=UserProfile)
def get_profile_by_id(user_id: int):
    return scraper.get_profile_by_id(user_id)


@app.post("/api/profiles", response_model=list[UserProfile])
def get_profiles(payload: UserIDList):
    return scraper.get_profiles_by_ids(payload.user_ids)


@app.get("/api/search", response_model=list[UserProfile])
def search_users(name: str):
    return scraper.get_users_by_name(name)


@app.post("/api/export/by-ids")
def export_profiles_by_ids(payload: UserIDList):
    users = scraper.get_profiles_by_ids(payload.user_ids)
    scraper.export_users(users)

    return {
        "status": "ok",
        "exported": len(users),
        "path": scraper.fs_manager.get_user_json_path()
    }


@app.get("/ping")
def ping():
    return {'ping': 'pong!'}


if __name__ == "__main__":
    uvicorn.run("api.main:app", host=UVICORN_HOST, port=UVICORN_PORT, reload=True)
