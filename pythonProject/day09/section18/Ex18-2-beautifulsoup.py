'''https://movie.naver.com/movie/bi/mi/basic.nhn?code=10016

프로토콜: 통신규약
         https/http - Hyper Text Transfer Protocol 웹 서버 접속
         ftp - 파일 서버 접속
         mailto - 전자메일 서버 접속
         talnet - 원격지 접속

호스트 주소(host) - 웹페이지를 요청할 서버의 이름
        ex) movie.naver.com

경로(path) - 웹서버에서 자원에 대한 경로
        ex)/movie/bi/bi/basic.nhn

쿼리(query) - 추가로 서버에 보내는 파라미터
        ex)code=10016
           key1=value1&key2=value2

'''

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 10016}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

review_list = soup.find_all('div',class_= 'score_reple')

for review in review_list:
    print(review.find('p').text.strip())