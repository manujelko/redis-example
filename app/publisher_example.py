import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

    channel = "my-channel"
    while True:
        message = input("Enter a message: ")
        await redis.publish(channel, message)
        if message.lower() == "exit":
            break

    # Close the connection
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
