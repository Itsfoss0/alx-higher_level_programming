#!/bin/bash
# Send JSON data to a server specified in the args
curl -s -X POST --header "Content-Type: Application/json" $1" --json "$2"
