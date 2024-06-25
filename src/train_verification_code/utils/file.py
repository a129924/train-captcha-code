def write_file(
    text: str,
    out_filapath: str,
    mode: str = "w+",
    encoding: str = "UTF-8",
) -> None:
    with open(out_filapath, mode=mode, encoding=encoding) as file:
        file.write(text)
