#!/usr/bin/python3
"""Send a request to the url and print the response"""

from urllib import request, error
from sys import argv


def request_header_property(url: str) -> str:
    """
    Send a request to the URL specified and
    get the response and handle exceptions
    Args:
        url (str): The URL to query
    """
    try:
        with request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except error.HTTPError as e:
        return "Error code: {}".format(e.code)


if __name__ == "__main__":
    print(request_header_property(argv[1]))
