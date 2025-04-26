from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tweeterpy import TweeterPy, config

twitter = TweeterPy()
app = FastAPI()

twitter.update_api(False)
twitter.generate_session(auth_token="5816384c85fb2734fd87ecbbe302a08f9ef80bed")

@app.get("/")
async def root():
    return twitter.search("elonmusk")

@app.get("/SearchTimeline")
async def get_user_info(rawQuery):
    search_query = rawQuery
    return twitter.search(search_query)
