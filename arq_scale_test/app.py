import asyncio

from arq import create_pool

from .config import settings


async def create_jobs(num: int) -> None:
    redis = await create_pool(settings.ARQ_REDIS_SETTINGS)

    for i in range(num):
        job = await redis.enqueue_job("long_running_func")
        assert job is not None
        print(f"{i + 1}: Job ID: {job.job_id} | {await job.status()}")


if __name__ == "__main__":
    asyncio.run(create_jobs(5))
