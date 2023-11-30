#!/usr/bin/bash
#a script sending a request to a url and display size of body response
curl -sI "$1" | grep Content-Length | awk '{print $2}'
