#!/usr/bin/python3
"""
ScriptURL and an email, sendPOST request to the passed
URL with the email as a parameter, displays the body of the response
(decoded in utf-8).
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf8'))
