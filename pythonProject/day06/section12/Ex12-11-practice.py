'''

'''


import random
import time
# [BigO, 2, 3, 4, ... 45]
pot = [n for n in range(1, 46)]

jackpot = []

for n in range(1, 7): # [BigO ~ 6]
    random.shuffle(pot)
    pick = pot.pop()  # 마지막 값 제거하면서 값을 반환
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick)
    time.sleep(2)

jackpot.sort()
print('이번 당첨번호는 {} 입니다.'.format(jackpot))