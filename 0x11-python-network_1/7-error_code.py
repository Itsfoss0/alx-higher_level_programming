#!/usr/bin/python3
"""Send a request to the url and print the response"""

from requests import get
from sys import argv


def request_header_property(url: str) -> str:
    """
    Send a request to the URL specified and
    get the response and handle exceptions
    Args:
        url (str): The URL to query
    """
    response = get(url)
    if int(response.status_code) >= 400:
        return ("Error code: {}".format(response.status_code))

    return response.text


if __name__ == "__main__":
    print(request_header_property(argv[1]))
