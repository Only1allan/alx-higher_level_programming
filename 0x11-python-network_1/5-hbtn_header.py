#!/usr/bin/python3
"""script takes in a URL, sends a request and displays value of X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
