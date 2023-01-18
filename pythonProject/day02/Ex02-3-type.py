'''

내장 데이터 유형
   python 변수는 다른 유형의 데이터를 저장할 수 있으며
   다른 유형은 다른 작업을 수행할 수 있다.


텍스트 유형 : str
숫자 유형 : int, float, complex
시퀀스 유형 : list, tuple, range
매핑 유형 : dict
세트 유형 : set
부울(논리) 유형 : bool
바이너리 유형 : bytes, bytearray
없음 유형 : NoneType

'''

# str = 문자열
x = "Hello World"
print(type(x))

# int = 정수
x = 20
print(type(x))

# float
x= 20.5
print(type(x))

# complex = 복소수
x = 1j
print(type(x))

# list = 메모리 영역의 위치를 알 수 있음, 입력값을 변경할 수 있다
x = ["피카츄", "라이츄", "파이리"]

# tuple = 입력값을 변경할 수 없다
x = ("피카츄", "라이츄", "파이리" )

# range =
x = range(6)
print(type(x))

# dict
x = {"name":"피카츄", "기술":"백만볼트!"}
print(type(x))

# set = 순서x
x = {"피카츄", "라이츄", "파이리"}
print(type(x))

# bool(논리) true or false
x = True #False
print(type(x))

# NoneType
d = None
print(type(d))

# 숫자 + 숫자 = 숫자
# 문자 + 숫자 + 문자숫자

num1 = 10
num2 = 20
result = num1 + num2
print(result)
name = 'Alice'
age = '15'
result = name + '/' + age
print(result)