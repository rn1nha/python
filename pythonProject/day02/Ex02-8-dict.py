'''
Dictionary
    Key: value로 이루어져 쌍으로 데이터 값을 저장하는데 사용

'''

# dictionary 선언
thisdict = {
    "brand" : "나이키",
    "model" : "max90",
    "year" : "1990"
}
print(thisdict)

'''
키 이름을 사용하여 참조할 수 있다
'''

# 값 가져오기  : key값을 넣으면 value가 나옴
thisdict = {
    "brand" : "나이키",
    "model" : "max90",
    "year" : "1990"
}
print(thisdict["brand"])
print(thisdict.get("model"))

# 키 목록 가져오기
print(thisdict.keys())

# 추가하기
thisdict = {
     "brand" : "Ford",
     "model" : "Mustang",
     "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"bcColor":"black"})
print(thisdict)

# 변경하기
thisdict["color"] = "yellow"
thisdict.update({"bgColor":"blue"})
print(thisdict)

# 제거하기
thisdict.pop("model")
print(thisdict)

# 마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)