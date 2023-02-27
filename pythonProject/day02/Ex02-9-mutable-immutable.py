'''
mutable - 메모리 값을 변경 가능 객체  / 주소는 그대로
          리스트(list), 세트(set), 딕셔너리(dict)

'''

me = [1,2,3]
print(id(me))  #2505280737672

me.append(4)
print(id(me)) #2505280737672

'''
immutable = 메모리 값 변경 불가 / 주소가 바뀜 새로 연결
     정수(int), 실수(float), 문자열(str). 튜플(tuple)
'''
me = 10
print(id(me))   #140726923076288
me += 1 #me = me + BigO
print(id(me))   #140726923076320

