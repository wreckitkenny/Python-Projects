#!/usr/bin/env python3
import requests
import sys

access_token = sys.argv[1]

_request_url = "https://graph.facebook.com/me"
_parameter = {"fields": "id,name,birthday,email", "access_token": access_token}
_get = requests.get(_request_url, params=_parameter)
_info = _get.json()

print("""
====== Facebook Information ======
+ Name: {}
+ ID: {}
+ BOD: {}
+ Email: {}""".format(_info["name"], _info["id"],
                      _info["birthday"], _info["email"]))
