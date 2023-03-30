#!/bin/bash
#send a bash script to a URL and display the body of the response
curl -sL --fail -X GET "$1";
