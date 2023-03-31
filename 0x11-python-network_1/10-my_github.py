#!/usr/bin/python3
"""
module to print ones github id
One will need GH PAT for this
"""

from requests import get
from sys import argv
from requests.auth import HTTPBasicAuth


def get_github_id(username: str, tokken: str) -> str:
    """
    get the user id of a github user
    Args:
        username (str): github handle
        tokken (str): the personal access tokken
    """
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": "Bearer {}".format(tokken),
        "User-Agent": "I am the Cavalry"
    }
    auth = HTTPBasicAuth(username, tokken)
    response = get("https://api.github.com/user", headers=headers, auth=auth)
    return response.json().get('id')


if __name__ == "__main__":
    print(get_github_id(argv[1], argv[2]))
