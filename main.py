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

@app.get("/TweetDetail")
async def TweetDetail(restId, authToken, ct0, cursor = None):
    client = Client("en-US")
    client.set_cookies({
        "auth_token": authToken,
        "ct0": ct0,
    })
    response, _ = await client.gql.tweet_detail(
        tweet_id=restId,
        cursor=cursor
    )
    return response

@app.get("/CommunityTweetsTimeline")
async def CommunityTweetsTimeline(authToken, ct0, communityId, rankingMode = "Recency", cursor = None, count = 20):
    client = Client("en-US")
    client.set_cookies({
        "auth_token": authToken,
        "ct0": ct0,
    })
    response, _ = await client.gql.community_tweets_timeline(
        community_id = communityId,
        ranking_mode = rankingMode,
        count = count,
        cursor = cursor
    )
    return response

@app.get("/UserTweetsAndReplies")
async def UserTweetsAndReplies(authToken, ct0, restId, cursor = None):
    client = Client("en-US")
    client.set_cookies({
        "auth_token": authToken,
        "ct0": ct0,
    })
    response, _ = await client.gql.user_tweets_and_replies(
       user_id = restId,
       cursor = cursor,
       count = 20
    )
    return response

@app.get("/ListLatestTweetsTimeline")
async def ListLatestTweetsTimeline(authToken, ct0, listId, cursor = None, count = 20):
    client = Client("en-US")
    client.set_cookies({
        "auth_token": authToken,
        "ct0": ct0,
    })
    response, _ = await client.gql.list_latest_tweets_timeline(
        list_id = listId,
        cursor = cursor,
        count = count
    )
    return response