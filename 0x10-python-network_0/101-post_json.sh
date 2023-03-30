#!/bin/bash
# Send JSON data to a server specified in the args
curl --json -d "$(cat "$2")" -s -X POST --header "Content-Type: application/json" "$1"
