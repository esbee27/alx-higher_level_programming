#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    req = requests.post(url, values)
    print(req.text)
