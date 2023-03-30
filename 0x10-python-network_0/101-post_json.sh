#!/bin/bash
# Send JSON data to a server specified in the args
curl -s -X POST "$1" --json "$2"
