'''
버블정렬(Bubble sort)
   인접한 두 원소를 비교하여 정렬하는 알고리즘 중 하나로
   가장 간단한 정렬 알고리즘 중 하나

   버블 정렬의 시간복잡도는 0(n^2)
'''

def bubble_sort(arr):
    n = len(arr)   # 배열의 길이
    for i in range(n):  # 0부터 n-1 까지 반복
        for j in range(n-i-1): # 0부터 n - i -2까지 반복
            if arr[j] > arr[j+1]:  # 인접한 두 원소를 비교
                # 앞의 원소가 뒤의 원소보다 크면 두 원소의 위치를 변경
                # arr[j], arr[j+1] = arr[j+1], arr[j]
                # tmp(임시 변수)가 필요
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


    return arr

# 실행코드

arr = [ 6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort(arr))