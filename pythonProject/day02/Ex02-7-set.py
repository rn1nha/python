'''
set
  순서가 없음
  인덱싱 되지 않는 컬렉션
  중복값 없음
'''
thisset = {"피카츄", "라이츄", "파이리"}
# 실행할 때 마다 순서가 변경
print(thisset)

# 항목 가져오기
for x in thisset:   # thisset 길이만큼 반복
     print(x)

# 값이 있는지 확인 in
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset) #True
print("꼬부기" in thisset)  #False

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤즈"}
thisset1.update(thisset2)
print(thisset1)

# 항목제거 remove -> 없는 항목 제거하면 에러 discard -> 없는 항목을 제거해도 에러 x
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

# 항목 제거 pop -> set에는 순서가 없어서 랜덤으로 하나씩 삭제
thisset.pop()
print(thisset)

#비우기
thisset.clear()
print(thisset)

