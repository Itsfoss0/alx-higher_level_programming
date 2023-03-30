#!/bin/bash
# send a GET request to the arg specified with a custom header
curl -s -X GET --header "X-School-User-Id: 98" "$1"
