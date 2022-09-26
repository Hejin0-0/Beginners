# NMT(Neural Machine Translation) : 인공신경망 기반 기계 번역
# SMT(Statistical Machine Translation) : 통계 기반 기계 번역
# 레퍼런스 : https://developers.naver.com/docs/papago/papago-nmt-api-reference.md#%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0

import os
import sys
import urllib.request
import json
from pprint import pprint

# 번역할 메모장 불러오기
with open(
    "/Users/lovenstein/Documents/Python/web crawling/04 Rest API - requests/source.txt",
    "r",
    encoding="utf-8",
) as f:
    srcText = f.read()

client_id = "G2sIRGjQ_NQUvQJzpusT"  # 개발자센터에서 발급받은 Client ID 값
client_secret = "ZW5ryb6nNt"  # 개발자센터에서 발급받은 Client Secret 값

encText = urllib.parse.quote(srcText)
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    # json 형 변환
    res = json.loads(response_body.decode("utf-8"))
    from pprint import pprint

    pprint(res)

    # 파일 생성
    with open("translate.txt", "w", encoding="utf-8") as f:
        f.write(res["message"]["result"]["translatedText"])

else:
    print("Error Code:" + rescode)
