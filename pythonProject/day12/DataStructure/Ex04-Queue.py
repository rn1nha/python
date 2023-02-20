'''
큐(queue)
    컴퓨터의 기본적인 자료 구조의 한가지로,
    먼저 집어 넣은 데이터가 먼저 나오는
    FIFO(First In First Out) 구조로 지정하는 형식을 말함
'''

def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print(queue)
    while queue:
        print("Get Value:",queue.pop(0))   #매개변수 설정

Queue()