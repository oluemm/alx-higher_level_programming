#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
# import urllib.parse

if __name__ == "__main__":
    # open the given url and alias it as response
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        # read the contents of response and save as html variable
        html = response.read()
        # check te type of the html content
        c_type = type(html)
        # parse from byte to utf8
        # utf8_ctn = urllib.parse.quote_from_bytes(html)
        utf8_ctn = html.decode('utf-8')

        print(f"Body response:\
            \n\t- type: {c_type}\
                \n\t- content: {html}\
                    \n\t- utf8 content: {utf8_ctn}")
