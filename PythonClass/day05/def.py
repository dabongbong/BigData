# 함수
# 기능, 클래스 안에서는 메서드라고 부른다

import urllib.request

def getweb(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹페이지 주소를 입력하세요 >')
print(getweb(url))