#!/bin/bash
# a script sends a POST request to the passed URL, and displays the body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
