import asyncio
from typing import Any

from .config import settings


async def long_running_func(
    ctx: dict[Any, Any] | None,
) -> None:
    await asyncio.sleep(60)


def worker_dispatcher():
    class ArqWorker:
        # Functions to schedule
        functions = [long_running_func]

        # ARQ settings
        redis_settings = settings.ARQ_REDIS_SETTINGS
        max_jobs = settings.ARQ_MAX_JOBS
        job_timeout = settings.ARQ_JOB_TIMEOUT
        keep_result = settings.ARQ_KEEP_RESULT
        max_tries = settings.ARQ_MAX_TRIES
        health_check_interval = settings.ARQ_HEALTH_CHECK_INTERVAL
        retry_jobs = settings.ARQ_RETRY_JOBS
        allow_abort_jobs = settings.ARQ_ALLOW_ABORT_JOBS

    return ArqWorker


worker0 = worker_dispatcher()
worker1 = worker_dispatcher()
worker2 = worker_dispatcher()
worker3 = worker_dispatcher()
worker4 = worker_dispatcher()
