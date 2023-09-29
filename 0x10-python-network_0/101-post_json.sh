#!/bin/bash
#script that send JSON POST and displays body of response
curl -s "$1" -X POST -H -d @"$2" "Content-Type: application/json"
