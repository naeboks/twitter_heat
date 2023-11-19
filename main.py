import aiohttp
import asyncio
from random_words import RandomWords
from typing import List

from better_automation import TwitterAPI


async def twitter_demo(token: str, user_handles: List[str], tweet_ids: List[int]):
    async with aiohttp.ClientSession() as session:
        twitter = TwitterAPI(session, token)
        username = await twitter.request_username()
        print(f"Your username: {username}")
        for user_handle in user_handles:
            user_id = await twitter.request_user_id(user_handle)
            print(f"{user_handle} is followed: {await twitter.follow(user_id)}")

        # for tweet_id in tweet_ids:
        #     await twitter.like(tweet_id)
        #     await twitter.repost(tweet_id)


async def main():
    async with aiohttp.ClientSession() as session:
        with open('tokens.txt') as f:
            tokens = f.read().splitlines()

        with open('users.txt') as f:
            users = f.read().splitlines()

        with open('posts.txt') as f:
            tweets = f.read().splitlines()
            tweets = [int(tweet) for tweet in tweets]

        for token in tokens:
            await twitter_demo(token, users, tweets)


if __name__ == '__main__':
    asyncio.run(main())
