#!/usr/bin/python
"""
module for a script to send a request to the URL passed
in the arguments and print the value of
X-Request-Id header
"""

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
