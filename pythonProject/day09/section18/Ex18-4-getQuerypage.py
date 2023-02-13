'''
request -> 서버 요청
response -> 서버 응답

http 응답(response)코드
  200번대 응답 : 성공(Success)
  300번대 응답 : 리다이렉션(Redirection)
  400번대 응답 : 클라이언트 에러(Client Error)
     Ex) 404 찾을 수 없는 페이지
  500번대 응답 : 서버 에러(Server Error)
     Ex) 503 서버가 요청을 처리할 준비가 되지 않음

'''

import requests

url = 'https://www.naver.com'
response = requests.get(url)
print('응답 코드: {}'.format(response.status_code))
print(response.text)