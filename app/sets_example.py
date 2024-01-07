import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    # Add elements to a set
    await redis.sadd("myset", "a", "b", "c")

    # Check if an element is in the set
    is_member = await redis.sismember("myset", "a")
    print(f"'a' is a member of set: {is_member}")

    # Get all memebers of the set
    members = await redis.smembers("myset")
    print(f"Set members: {members}")

    # Close the connection
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
