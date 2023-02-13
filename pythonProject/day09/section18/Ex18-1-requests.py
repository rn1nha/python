'''
모듈 설치 requests
pip install requests
pip install chardet
pip install brotli

conda install requests
'''

import requests

url = 'http://movie.naver.com/movie/bi/mi/basic.nhn'  # 페이지 주소 - 사이트 접속
param = {'code': 161967}  #데이터를 매개변수로
response = requests.get(url, params=param)
print(response.text)