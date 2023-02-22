'''

  시간복잡도
      알고리즘 실행에 걸리는 시간을 분석하는 방법
      시간복잡도를 표현하는 대표적인 세가지 표기법

    빅오(Big O), 빅오메가(Big Omega), 빅세타(Big Theta)

빅오(Big O) : 알고리즘의 최악의 경우(최대 입력 크기) 실행 시간의 상한선을 타나냄

빅오메가(Big Omega) : 알고리즘의 최선의 경우(최소 입력 크기) 실행 시간의 하한선을 나타냄

빅세타(Big Theta) : 알고리즘의 최선과 최악 경우 실행 시간의 상한과 하한 모두 나타냄


O(BigO) : 상수시간 복잡도
'''

def return_first_value(arr):
    return arr[0]

#실행 코드
arr = [1, 3, 5, 7, 8]

print(return_first_value(arr))