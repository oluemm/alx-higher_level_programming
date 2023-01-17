#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        # manually strolling thru the response to get
        # filter out required header
        X_Request_d = (response.__dict__.get('headers')
                       .__dict__['_headers'][-3][1])
        # a more sustainable approach
        X_Request_d = dict(response.headers).get("X-Request-Id")
        print(f"{X_Request_d}")
