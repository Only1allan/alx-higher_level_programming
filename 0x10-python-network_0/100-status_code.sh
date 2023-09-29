#!/bin/bash
#script sending a request to url and displays status code
curl -s -o /dev/null -w "%{http_code}" "$1"
