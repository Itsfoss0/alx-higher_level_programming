#!/bin/bash
#send a POST request to a server specifed as an arg
curl -s -X POST --data "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1";
