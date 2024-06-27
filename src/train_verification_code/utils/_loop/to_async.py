from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


async def to_async(
    func: Callable[..., T],
    *args: Any,
    executor: Optional[ThreadPoolExecutor] = None,
) -> T:
    from asyncio import get_event_loop

    loop = get_event_loop()

    return await loop.run_in_executor(executor, func, *args)
