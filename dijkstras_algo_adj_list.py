import heapq

class Node:
    
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.min_value = float('inf')
        self.adjacency_list = list() # gotta add edges here
        self.visited = False

    def __lt__(self, other_node):
        return self.min_value < other_node.min_value

class Edge:
    
    def __init__(self, weight, origin_vertex, target_vertex) -> None:
        self.origin_vertex = origin_vertex
        self.target_vertex = target_vertex
        origin_vertex.adjacency_list.append(self)
        self.weight = weight

class DijkstrasAlgorithm:
    def __init__(self) -> None:
        self.heap = list()
    
    def calculate(self, start_vertex):
        start_vertex.min_value = 0
        heapq.heappush(self.heap, start_vertex)
        
        while self.heap:
            
            actual_node = heapq.heappop(self.heap)
            
            if actual_node.visited:
                continue
            
            for edge in actual_node.adjacency_list:
                org = edge.origin_vertex
                dest = edge.target_vertex
                heapq.heappush(self.heap, dest)
                        
                if org.min_value + edge.weight < dest.min_value:
                    dest.min_value = org.min_value + edge.weight
                    dest.predecessor = org
            
            actual_node.visited = True
    
    def min_path(self, vertex):
        print("the shortest distance from source vertex to given vertex is {} ".format(vertex.min_value))
        actual = vertex
        while actual:
            print(F"{actual.name}", end= ' -> ' if actual.predecessor else '')        
            actual = actual.predecessor

    
if __name__ == "__main__":
    #create vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    
    #edges
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    #dijkstras 
    algo = DijkstrasAlgorithm()
    algo.calculate(node1)
    algo.min_path(node7)