#!/usr/bin/python3

"""
send a GET request to a the url provided
as an Argument to the script and print the
X-Request-Id value of the header
"""


from requests import get
from sys import argv


def get_alx_intranet(url):
    """
    Send a GET request to the url
    and print the X-Request-Id header value
    """
    return get(url).headers['X-Request-Id']


if __name__ == "__main__":
    print(get_alx_intranet(argv[1]))
