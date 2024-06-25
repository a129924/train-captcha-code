def fetch_url(url: str, timeout: float = 30):
    from urllib.request import urlopen, Request

    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    request = Request(url=url, headers=headers)

    with urlopen(url=request, timeout=timeout) as response:
        if status_code := response.getcode() in {200, 201, 202, 203, 204}:
            return response.read()

        from urllib.error import HTTPError

        raise HTTPError(
            url=url,
            code=status_code,
            msg="error response",
            hdrs=headers,  # type: ignore
            fp=None,
        )
