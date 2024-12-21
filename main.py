from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tweeterpy import TweeterPy
import logging

app = FastAPI()
twitter = TweeterPy()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# get user info by screen name
@app.get("/user/screen_name/{twitter_user_screen_name}")
async def get_user_info(twitter_user_screen_name):

    try:
        user_data = twitter.get_user_data(twitter_user_screen_name)
        return user_data
    except Exception as e:
        print("retry: " + twitter_user_screen_name)

        try: 
            twitter.generate_session()
            user_data = twitter.get_user_data(twitter_user_screen_name)
            return user_data
        except Exception as e:
            logging.error(e)
            return JSONResponse(
                status_code=400,
                content={"message": "can't find user"}
            )
