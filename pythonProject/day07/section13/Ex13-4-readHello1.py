'''
r (read mode) : 읽기 전용 모드 | 파일 없으면 에러

경로
   절대경로 ㅣ ex) C:\pythonProject\rrr\pythonProject\day07\section13
   상대경로 | ex) ./upload/hello2.txt
                ../../resources/hello.txt
       . -> 현재 폴더
       .. -> 상위 폴더
'''

file = open('../../resources/hello.txt', 'rt' )
str = file.read()
print(str, end='')
file.close()

# file = open('hello.txt', 'rt',)
# str = file.read()
# print(str, end='')
# file.close()
