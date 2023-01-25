'''
for문
   값의 범위나 횟수가 정해져 있을 때
   사용하면 편리한 반복문
   while문 보다 자주 사용

for 변수 in 반복가능개체 :
    반복실행문
'''

pwd = 'abcdefg55'

ch_count = 0   #7
num_count = 0   #2
for ch in pwd:
    if ch.isalpha():  #알파벳 인지 아닌지 bool 타입으로 반환
        ch_count += 1
    elif ch.isnumeric(): #숫자 인지 아닌지 bool 타입으로 반환
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    Print('불가능한 비밀번호 입니다.')