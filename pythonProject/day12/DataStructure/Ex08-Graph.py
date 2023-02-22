'''
그래프(Graph)
  노드(vertice)와 간선(정점/edge/arcs)로 이루어진 자료구조
'''

class Graph:
    def __init__(self,vertices):
        # 생성자 함수, 그래프 객체 생성 시 호출됨
        self.vertices = vertices # 그래프의 정점 리스트
        self.adj_list = {} # 인접 리스트(해시 테이블)
        for vertex in vertices:
            self.adj_list[vertex] = [] # 초기화 -

    def add_edge(self, u, v):
        #
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, end = ' -> ')
            print(' -> '.join([str(node)for node in self.adj_list[vertex]]))

vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.print_graph()