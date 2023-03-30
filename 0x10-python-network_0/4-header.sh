#!/bin/bash
# send a GET request to the arg specified with a custom header
curl -X GET --header "X-School-User-Id: 89" "$1"
