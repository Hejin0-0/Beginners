import os
import sys
import requests
from pprint import pprint
import json

client_id = "G2sIRGjQ_NQUvQJzpusT"
client_secret = "ZW5ryb6nNt"

url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지
# url = "https://openapi.naver.com/v1/vision/celebrity"  # 유명인 얼굴인식

files = {
    "image": open(
        "/Users/lovenstein/Documents/Python/web crawling/04 Rest API - requests/test.jpg",
        "rb",
    )
}
headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

response = requests.post(url, files=files, headers=headers)
rescode = response.status_code

if rescode == 200:
    # print(response.text)
    data = json.loads(response.text)
    pprint(data)
    print(type(data))
    print(data["info"]["faceCount"])
else:
    print("Error Code:" + rescode)
