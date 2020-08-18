#!/bin/bash
# script sends a DELETE request URL passed as the first arg and display body the response
curl -sX DELETE "$1"
