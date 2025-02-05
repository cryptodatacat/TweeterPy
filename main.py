from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tweeterpy import TweeterPy, config
from twikit import Client
from twikit.guest import GuestClient

import logging
import random

client = GuestClient('en-US')

app = FastAPI()
clients = [
    TweeterPy(),
]

@app.get("/")
async def root():
    await client.activate()
    user = await client.get_user_by_screen_name('elonmusk')

    return user.name

# get user info by screen name
@app.get("/user/screen_name/{twitter_user_screen_name}")
async def get_user_info(twitter_user_screen_name):
    t = random.choice(clients)
    
    try:
        user_data = t.get_user_data(twitter_user_screen_name)
        return user_data
    except Exception as e:
        print("retry: " + twitter_user_screen_name)

        try: 
            t.generate_session()
            t2 = random.choice(clients)
            # t.request_client.session.proxies = proxies_formatted
            user_data = t2.get_user_data(twitter_user_screen_name)
            return user_data
        except Exception as e:
            print("error: " + twitter_user_screen_name)

            logging.error(e)
            return JSONResponse(
                status_code=400,
                content={"message": "can't find user"}
            )
