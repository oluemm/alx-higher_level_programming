#!/usr/bin/python3
"""script that sends a request to the URL and displays the value of the 
X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        # a more sustainable approach
        X_Request_d = response.headers.get("X-Request-Id")
        print(f"{X_Request_d}")
