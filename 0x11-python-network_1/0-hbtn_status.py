#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


def fetchdata():
    """fetches data"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

if __name__ == "__main__":
    fetchdata()
