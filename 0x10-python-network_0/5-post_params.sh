#!/bin/bash
#script that sends POST request to URL and displays body of response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
