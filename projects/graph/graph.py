"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Queue for visited nodes
        q = Queue()
        # Add starting node to queue
        q.enqueue(starting_vertex)
        # Set to track visited verts
        visited_vertices = set()

        # While queue still has verts still stored in it
        while q.size() > 0:
            # Get current vert from front of queue
            current_vertex = q.dequeue()

            # If current vert has not been visited
            if current_vertex not in visited_vertices:
                # Add vert to visited set
                visited_vertices.add(current_vertex)
                print(current_vertex)

                # Loop through neighboring verts of current vert
                for neighbor in self.get_neighbors(current_vertex):
                    # Add neighboring vert to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Stack for visited nodes
        s = Stack()
        # Add starting vert to stack
        s.push(starting_vertex)
        # Set to track visited verts
        visited_vertices = set()

        # While stack still has verts stored in it
        while s.size() > 0:
            # Get and set current vert to vert from top of stack
            current_vertex = s.pop()

            # If current vert has not been visted
            if current_vertex not in visited_vertices:
                # Add vert to visted set
                visited_vertices.add(current_vertex)
                print(current_vertex)

                # Loop through neighboring verts of current vert
                for neighbor in self.get_neighbors(current_vertex):
                    # Add neighboring vert to stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Stack for visited verts
        s = Stack()
        # Set to track visited verts
        visited_vertices = set()
        # List to track path beginning with starting vert
        path = [starting_vertex]
        # Add path to stack
        s.push(path)

        # While stack still has verts in it
        while s.size() > 0:
            # Get and set current path from top of stack
            current_path = s.pop()
            # Set current vert to last vert in current path
            current_vertex = current_path[-1]

            # If current vert is vert we are looking for
            if current_vertex == destination_vertex:
                # return path traveled
                return current_path

            # If vertex has not been visted
            if current_vertex not in visited_vertices:
                # Add vert to visited set
                visited_vertices.add(current_vertex)

            # loop through neighboring verts of current vert
            for neighbor in self.get_neighbors(current_vertex):
                # Make path for each neighbor and add to stack
                s.push(current_path + [neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
