import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

    # Add elements with scores
    await redis.zadd("myzset", {"a": 1, "b": 2, "c": 3})

    # Get elements with scores between a range
    elements = await redis.zrangebyscore("myzset", min=1, max=2, withscores=True)
    print(f"Elements in score range: {elements}")

    # Close the connection
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
