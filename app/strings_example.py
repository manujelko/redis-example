import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    # Set a key
    await redis.set("mykey", "Hello, Redis!")

    # Get a key
    value = await redis.get("mykey")
    print(f"The value of 'mykey' is: {value}")

    # Close the connection
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
