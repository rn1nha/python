# Join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

# split() 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)
print(result[2])

data = '김민하|25|프로그래머'
result = data.split('|')
print(result)
print('이름 : {}'.format(result[0]))

# replace() 메소드
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '      apple'
print(s)
result = s.lstrip() #왼쪽 공백 제거
print(result)

s = 'apple       '
print(s)
result = s.rstrip()
print(result)

s = '         apple      '
print(s)
result = s.strip()
print(result)

s = ' a p p l e '
print(s)
result = s.strip()  #앞 뒤의 공백만 제거
print(result)
result = s.replace(' ', '')
print(result)
