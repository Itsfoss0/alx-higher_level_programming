#!/usr/bin/python3

from urllib.request import urlopen
from urllib.error import URLError
"""
Fetch https://alx-intranet.hbtn.io/status
and print the formated content to stdout
"""


def request_holberton() -> None:
    """
    Send a request to https://alx-intranet.hbtn.io/status
    Args:
        None
    Return:
        None
    """
    try:
        with urlopen('https://alx-intranet.hbtn.io/status') as response:
            response = response.read()
            print("Body response:")
            print("\t - type: {}".format(type(response)))
            print("\t - content: {}".format(response))
            print("\t - utf-content: {}".format(response.decode('UTF-8')))
    except URLError:
        print("Check your connection and try again.")


if __name__ == "__main__":
    request_holberton()
