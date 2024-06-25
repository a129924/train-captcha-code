def write_file_from_byte_string(
    text: str,
    out_filapath: str,
    mode: str = "wb",
) -> None:
    from base64 import b64decode

    with open(out_filapath, mode=mode) as file:
        file.write(b64decode(text.split(",", 1)[1]))
