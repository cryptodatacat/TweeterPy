from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tweeterpy import TweeterPy, config

config.UPDATE_API = False
twitter = TweeterPy()

app = FastAPI()

@app.get("/")
async def root():
    return "elonmusk"

@app.get("/SearchTimeline")
async def get_user_info(rawQuery, authToken):
    twitter.generate_session(auth_token=authToken)
    search_query = rawQuery
    return twitter.search(
        search_query = search_query,
        search_filter = "Latest",
        pagination = False
    )
