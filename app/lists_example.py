import asyncio

import aioredis


async def main():
    # Connect to Redis
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )

    # Push elements to the end of a list
    await redis.rpush("mylist", "element1", "element2", "element3")

    # Pop the last element
    last_element = await redis.rpop("mylist")
    print(f"Last element: {last_element}")

    # Get a range of elements from the list
    lst = await redis.lrange("mylist", 0, -1)
    print(f"List range: {lst}")

    # Close the connection
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
