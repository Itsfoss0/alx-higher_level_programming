#!/usr/bin/python3
"""Find the value of the X-Request-Id in response"""

from urllib import request, error
from sys import argv


def request_header_property(url: str) -> str:
    """
    Send a request to the URL specified and
    get the response headers
    Args:
        url (str): The URL to query
    """
    try:
        with request.urlopen(url) as response:
            return response.info()['X-Request-Id']
    except error.URLError as e:
        return e.reason


if __name__ == "__main__":
    print(request_header_property(argv[1]))
