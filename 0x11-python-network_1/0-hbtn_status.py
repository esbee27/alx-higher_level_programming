#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\- type: "{}.format(type(response)))
        print("\- content: "{}.format(body))
        print("\- utf8 content: "{}.format(body.decode("utf-8")))

if __name__ == "__main__":
