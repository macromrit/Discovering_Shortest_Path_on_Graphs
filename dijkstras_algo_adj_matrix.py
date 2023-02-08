import sys

class DijkstraAlgorithm:
    def __init__(self, adjacency_matrix, start_vertex):
        #if 0 then no connection
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)#no. of vertices
        self.visited = [False for _ in range(len(adjacency_matrix))] 
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0
    
    def get_min_vertex(self):
        
        #find the vertex with lowest distance value
        min_vertex_value = sys.maxsize
        min_vertex_index = 0
        
        #linear serach in O(N) time cmplxty
        for index in range(self.v):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index

        return min_vertex_index

    def calculate(self):
        #we consider all the items in O(V) time complexity
        for vertex in range(self.v):
            actual_vertex = self.get_min_vertex()
            print(F"considering vertex {actual_vertex}")
            self.visited[actual_vertex] = True

            for other_vertex in range(self.v):
                #if there is a connection between two nodes
                if self.adjacency_matrix[actual_vertex][other_vertex]>0:
                    #is there a shorter path to the other_vertex from actual_vertex ?
                    if self.distances[actual_vertex] +self.adjacency_matrix[actual_vertex][other_vertex] < self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex]
    
    def print_distances(self):
        print(self.distances)


                     
            