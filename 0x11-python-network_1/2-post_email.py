#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    e_mail = {'email': sys.argv[2]}
    # encoding the url
    data = urllib.parse.urlencode(e_mail)
    # encoding the data as bytes
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        res_page = response.read()
        # decode the returned data
        decoded_page = res_page.decode('utf-8')
        print(decoded_page)
