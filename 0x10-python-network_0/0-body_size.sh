#!/bin/bash
#send a GET request to the url specified and print the size of response body to stdout
curl -sI $1" | head -n 5 | tail -n 1 | cut -d ":" -f 2
