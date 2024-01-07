import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    # Set multiple fields at once
    await redis.hset("myhash", mapping={"field1": "value1", "field2": "value2"})

    # Get a specific field's value
    value = await redis.hget("myhash", "field1")
    print(f"Value of field1: {value}")

    # Get all fields and values
    all_fields = await redis.hgetall("myhash")
    print(f"All fields: {all_fields}")

    # Close the connection
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
