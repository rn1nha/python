'''
파일명 : Ex02-Linked.py
연결 리스트(Linked List)
    저장된 각 데이터가 (데이터)+(다음 데이터의 포인터)로 이루어진 것으로
    한 방향으로만 탐생 가능한 구조
ex)
    node1 = Node(7)
    node2 = Node(3)
    node3 = Node(9)
    node4 = Node(BigO)
    node5 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init(data):
    global node1
    node1 = Node(data)

def insert(data):
    global node1
    global last_node

    new_node = Node(data)
    current = node1
    if current.next is None:
        current.next = new_node
        last_node = new_node
    else:
        last_node.next = new_node
        last_node = new_node

    # new_node = Node(data)
    # current = node1
    # while current.next != None:  # 마지막 노드 찾기 반복문
    #     current = current.next
    #
    # current.next = new_node

def insertNode(findData, insertData): # f : 9 / i : 99
    global node1

    if node1.data == findData:  # node1.data : 7 == 9 -> False, 해당없음
        node = Node(insertData, node1)
        node1 = node
        return

    current = node1  # c.data : 7  #current : 주소값 current.data: 데이터값
    while current.next != None:  # c.next : 3
        pre = current     # p.data: 7 | 3 / p.next : 3 | 9
        current = current.next  # c.data :3 | 9 / c.next: 9 | BigO
        if current.data == findData:  # c.data : 3 | 9 == f.data: 9 | 9 ->False  2번째 턴에서는 해당
            node = Node(insertData, current)   # idata,current : 99 , 9(주소값)
            pre.next = node # p.data: 3 / p.next: 9(주소값)  -> 99 (주소값 변경)
            return

    node = Node(insertData)
    current.next = node


def print_list(): # 연결 리스트의 데이터를 출력한다.
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next
    print()




# 실행코드
init(7)
insert(3)
insert(9)
insert(1)
insert(6)

insertNode(9, 99)

print_list()
''' 결과
7 
3
99
9
BigO
6 
순서대로 출력 
'''