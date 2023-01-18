'''
튜플
   단일 변수에 여러 항목을 저장하는데 사용됨
   순서가 있고, 변경할 수 없는 list
   둥근 괄호로 작성됨
'''

thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple)

# 튜플 길이
print(len(thistuple))

# 항목 접근
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])


# 튜플값 변경 방법 (억까 ㅋㅋ )
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple)  # casting(형변환)을 사용해 tuple을 list로 변환
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)

# 튜플 압축풀기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple
print(type(p1))
print(p2)
print(p3)
print(p4)

# 두개 튜플 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터풀", "야도란", "피존투", "또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)