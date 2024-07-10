#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter"""
from urllib import parse, request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    eml = parse.urlencode(values)
    data = eml.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        r = response.read()
        print(r.decode("utf-8"))
