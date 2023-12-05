#!/usr/bin/python3
"""script takes in a URL, sends a request and displays the value in header"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
