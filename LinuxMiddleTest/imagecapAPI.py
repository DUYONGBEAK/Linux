# 키 값을 받아오는 과정
import os
import sys
import urllib.request
client_id = "gDtrabHdY3dlTIg*****" # 개발자센터에서 발급받은 Client ID 값
client_secret = "3Rx9Sg****" # 개발자센터에서 발급받은 Client Secret 값
code = "0"
url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

# 결과 값에서 키값만 추출함
keyValue = response_body.decode('utf-8').split(':')[1][1:-2]

# 가져온 키값으로 이미지 캡차 실행
import os
import sys
import urllib.request
client_id = "gDtrabHdY3dlTIg*****" # 개발자센터에서 발급받은 Client ID 값
client_secret = "3Rx9Sg****" # 개발자센터에서 발급받은 Client Secret 값
key = keyValue # 캡차 Key 값
url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    print("캡차 이미지 저장")
    response_body = response.read()
    with open('captcha.jpg', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)
