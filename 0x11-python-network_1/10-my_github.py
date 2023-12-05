#!/usr/bin/python3
"""script takes your Github credentials and uses Github API to display id"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))
