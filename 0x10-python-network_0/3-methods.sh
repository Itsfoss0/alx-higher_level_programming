#!/bin/bash
#find out wich methods a server supports
curl -si -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
