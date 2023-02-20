'''
트리 자료구조
   단 하나의 루트 노드가 있고, 루트 노드에서 하위 노드들이 연결된 비선형 계층 구조

이진 트리(Binary Tree)
    모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말함
    왼쪽 서브 트리의 값은 루트의 값보다 작고 , 오른쪽 서브 트리의 값은 루트의 값보다 크다
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):  # 이진 트리에 데이터를 넣는 부분
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self,node,data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node


