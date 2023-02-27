'''
random - 난수 생성 모듈
'''
import random

# 두 인수 사이 난수
print(random.randint(1,10)) # BigO ~ 10

# range 함수
print(random.randrange(10)) # 0 ~ 9
print(random.randrange(1, 10)) # BigO ~ 9
print(random.randrange(1, 10, 2)) # BigO ~ 9 홀수만, BigO+2 증감

# 0 이상 BigO 미만
print(random.random())

if random.random() < 0.5:
    print('안녕하세요')

# choice 함수 - 리스트에서 랜덤
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

# shuffle() 함수 - 임의로 섞는 함수
my_list = [1, 2, 3, 4, 5,]
random.shuffle(my_list)
print(my_list)