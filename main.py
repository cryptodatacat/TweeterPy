from fastapi import FastAPI
from twikit import Client

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World"

@app.get("/SearchTimeline")
async def get_user_info(rawQuery, authToken, ct0, cursor = None):
    client = Client("en-US")
    client.set_cookies({
        "auth_token": authToken,
        "ct0": ct0,
    })

    response, _ = await client.gql.search_timeline(
        rawQuery, "Latest", 20, cursor)
    
    return response
