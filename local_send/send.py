import json
import os
import requests

files_t = {
    'file': ('new_1', open('./2020-06-28 12.csv', 'rb'))
}

headers = {'File-Name': 'new'}

r = requests.post(
    #'http://192.168.3.67:1234/upload',
    'http://127.0.0.1:8787/upload',
    files=files_t,
    headers=headers
)

print(r.text)
print(r)

