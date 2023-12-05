#!/usr/bin/python3
"""script takes 2 arguments in order to solve this challenge."""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
