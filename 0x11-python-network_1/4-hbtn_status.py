#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetchdata():
    """fetches data"""
    body = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
if __name__ == "__main__":
    fetchdata()
