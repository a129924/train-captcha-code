from typing import Optional


def current_executor(max_workers: Optional[int]):
    from concurrent.futures import ThreadPoolExecutor

    return ThreadPoolExecutor(max_workers=max_workers)
