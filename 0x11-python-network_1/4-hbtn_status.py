#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    # open the given url
    req = requests.get('https://alx-intranet.hbtn.io/status')
    # read the contents of response and save as html variable
    html = req.text  # resturns in plain unicode text
    # check te type of the html content
    c_type = type(html)
    # parse from byte to utf8
    # utf8_ctn = html.decode('utf-8')  # to decode bytes

    print(f"Body response:\n\t- type: {c_type}\n\t- content: {html}")
