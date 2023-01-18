#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in `utf-8`)"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]

    requestUrl = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(requestUrl) as response:
            decoded_page = response.read().decode('utf-8')
            print(decoded_page)
    except Exception as e:
        if hasattr(e, 'code'):
            print(f"Error code: {e.code}")
