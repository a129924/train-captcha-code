from collections.abc import Generator

from ..project_typing._typing import WriteFileState


def write_file_from_byte_string(
    text: str,
    out_filapath: str,
    mode: str = "wb",
) -> Generator[WriteFileState, None, None]:
    from base64 import b64decode

    try:
        file = open(out_filapath, mode=mode)
        file.write(b64decode(text.split(",", 1)[1]))

        yield WriteFileState(filepath=out_filapath, state="success")

    except Exception:
        yield WriteFileState(filepath=out_filapath, state="failed")

    finally:
        file.close()
