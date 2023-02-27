'''
이진 검색(Binary Search)
  데이터가 정렬되어 있는 상태에서 사용가능 알고리즘
  중앙 값과 비교하여 탐색 범위를 반으로 줄여가며 찾는 값을 탐색함
'''

def binary_search(arr, target):
    # 탐색 범위의 시작점과 끝점을 지정
      left, right = 0, len(arr) - 1
    # 탐색 범위가 존재하는 동안 반복함
      while left <= right:
          # 탐색 범위 중앙 인덱스를 계산함
          mid = (left + right) // 2
          #중앙 위치의 원소가 탐색 대상인 경우 인덱스를 반환함
          if arr[mid] == target:
              return mid
          #중앙 위치의 원소보다 탐색 대상이 적은 경우,
          #오른쪽 부분배열을 탐색한다
          elif arr[mid] > target:
              right = mid - 1
          #중앙 위치의 원소보다 탐색 대상이 큰 경우
          #왼쪽 부분배열을 탐색함
          else:
              left = mid + 1

      # 탐색 대상을 찾지 못한 경우 -1을 반환함
      return -1

# 실행 코드
arr=[1,3,5,7,8,99]
target = 7
result = binary_search(arr,target)
print(result)
