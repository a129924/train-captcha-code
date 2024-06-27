from ...project_typing._typing import WriteFileState


def write_file_from_byte_string(
    text: str,
    out_filapath: str,
    mode: str = "wb",
) -> WriteFileState:
    from base64 import b64decode

    try:
        file = open(out_filapath, mode=mode)
        file.write(b64decode(text))

        return WriteFileState(filepath=out_filapath, state="success")

    except Exception as error:
        print(error.__repr__())
        return WriteFileState(filepath=out_filapath, state="failed")

    finally:
        file.close()
