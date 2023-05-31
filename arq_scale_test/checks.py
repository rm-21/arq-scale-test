import asyncio

from arq import create_pool
from arq.jobs import Job

from .config import settings


async def job_status(task_id: str, stop: bool = False):
    job: Job = Job(
        job_id=task_id,
        redis=await create_pool(settings_=settings.ARQ_REDIS_SETTINGS),
    )

    print(f"ID {task_id}: {await job.status()}")

    if stop:
        result: bool = await job.abort()
        print(f"ID {task_id}: Aborted: {result}")


async def main():
    await job_status(task_id="b8057d4d790c42e48d58343140d7762a", stop=True)


if __name__ == "__main__":
    asyncio.run(main())
