#!/bin/bash
# display only the status code of a response
curl -o /dev/null -sIw "%{http_code}" "$1"
