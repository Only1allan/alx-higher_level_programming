#!/bin/bash
# a script send request to url, and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
