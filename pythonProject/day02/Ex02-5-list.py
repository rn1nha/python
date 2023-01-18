'''
List
   단일 변수에 여러 항목을 저장하는데 사용됨
   list 항목은 순서가 지정되고 변경가능하며 중복값 허용
   list 에는 다양한 데이터 유형이 포함될 수 있음
'''
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist)
print(thislist[0])
#print(thislist[0][0])  #피카츄에서 첫번째 변수를 가져온 것

# list 길이
print(len(thislist))

# list 데이터유형
list1 = ["피카츄", "라이츄", "꼬부기"]
list = [1, 2, 3, 4, 5]
list = [True, False, False]
# 다양한 유형 포함 가능
list4 = ["abc", 34, False, 40]

# 항목 접근
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1])

# 변경
thislist[1] = "잠만보"
print(thislist)

# 항목 변경 2개
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터풀", "야도란"]
thislist[1:3] = ["울먹이", "메타몽"]
print(thislist)

# 두번째 세번째 값을 하나의 값으로 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터풀", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)

# 항목 추가 [append]
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")
print(thislist)

# 항목추가 - 인덱스번호로 추가 [insert]
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, "잠만보")
print(thislist)

# 항목 값으로 제거 [remove]
thislist = ["피카츄", "라이츄", "파이리"]
thislist.remove("라이츄")
print(thislist)

# 항목을 지정된 인덱스로 제거 [pop]
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop(2)
print(thislist)

thislist = ["피카츄", "라이츄", "파이리", "잠만보"]
thislist.pop() #인덱스 값을 넣지 않으면 마지막 값이 삭제됨
print(thislist)

# 목록 삭제 [clear]
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear()
print(thislist)

# 확장 [extend]
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터풀", "야도란"])
print(thislist)

# 객체 삭제
#del thislist
#print(thislist) 에러가 남
