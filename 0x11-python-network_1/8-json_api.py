#!/usr/bin/python3
"""
Send a POST request to localhost:5000/search_user
with a query string and print the JSON result to
standard output
"""

from requests import post
from sys import argv


def send_query(query_string: str) -> str:
    """
    Send the POST questy_string to server
    Args:
        query_string (str): the query string
    Return:
        string
    """
    server = "http://0.0.0.0:5000/search_user"
    response = post(server, data={'q': query_string}).text
    try:
        resp_json = eval(response)
        if len(resp_json) != 0:
            return "[{}] {}".format(resp_json.get('id'), resp_json.get('name'))
        return "No result"
    except Exception as e:
        return "Not a valid JSON"


if __name__ == "__main__":
    if len(argv) >= 2:
        print(send_query(argv[1]))
    else:
        print(send_query(""))
