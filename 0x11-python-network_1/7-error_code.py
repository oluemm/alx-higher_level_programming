#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    decoded_page = response.text
    if hasattr(response, 'status_code') and response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(decoded_page)
