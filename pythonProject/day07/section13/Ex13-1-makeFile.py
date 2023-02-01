'''

파일 입출력(I/O - input/output)
     입력(input) 기존 파일 읽어 들이는 것
     출력(output) 파일 생성, 내용 추가를 말함
'''

# file = open('myFile.txt','wt')
# print('myFile.txt 파일이 생성되었습니다.')
# file.close()

# with문 ㅣ 자동으로 close()를 해줌
with open('myFile.text', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')