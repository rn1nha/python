'''
반복문
   어떤 수행 작업을 한 번이 아니라 계속해서 수행해야 할 때 사용

   반복문 종류
      while, for문

while문 : 특정 조건을 만족하는 동안 반복해서 수행하는 코드
while 조건식:
      반복 실행코드

'''
n = 10
while n >= 1:  # True -> False 될 때 까지 반복
    print(n)
    n -= 1

print("while 끝나고 n값 : {}".format(n))

