#!/usr/bin/python3
"""script takes in a URL and an email address, sends a POST request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    data = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
