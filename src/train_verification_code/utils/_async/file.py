from ...project_typing._typing import WriteFileState


async def write_file_from_byte_string(
    text: str,
    out_filapath: str,
    mode: str = "wb",
) -> WriteFileState:
    from .._loop.to_async import to_async
    from ..sync.file import write_file_from_byte_string

    return await to_async(write_file_from_byte_string, text, out_filapath, mode)
