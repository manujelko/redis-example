import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

    pubsub = redis.pubsub()
    channel = "my-channel"
    await pubsub.subscribe(channel)

    try:
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1)
            if message:
                print(f"Received: {message['data']}")
    except asyncio.CancelledError:
        await pubsub.unsubscribe(channel)
    finally:
        # Close the connection
        await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
