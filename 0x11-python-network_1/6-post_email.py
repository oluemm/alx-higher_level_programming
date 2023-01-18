#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    e_mail = {'email': sys.argv[2]}
    response = requests.post(url, data=e_mail)
    res_page = response.text
    print(res_page)
