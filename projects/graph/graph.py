"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # Vert ID --> set of neighbors
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        Vert_id will be key and will initialize a set as a value
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge from 1 vert to another
        Get vert1 from verts and add edge to vert2 in its set
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            print("Can't add edge to non extisting vert")
            return

        self.vertices[v1].add(v2)

    def remove_vertex(self, vertex_id):
        # Remove vert from graph and any incoming edges to it.
        if vertex_id not in self.vertices:
            print("Specified vertex is not in graph")
            return

        self.vertices.pop(vertex_id)

        for remaining_verts in self.vertices:
            self.vertices[remaining_verts].discard(vertex_id)

    def remove_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            print('One or more nodes not found in graph')
            return

        self.vertices[v1].discard(v2)

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
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            current_node = q.dequeue()

            if current_node not in visited:
                visited.add(current_node)
                print(current_node)

                for neighbor in self.vertices[current_node]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visited:
                visited.add(current_node)
                print(current_node)

                for neighbor in self.get_neighbors(current_node):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        **** If we don't pass set into the recursive call It will initialize a new empty set everytime
            therfore a node will never be marked visited and cause infinite recursion?

        **** There is not current node to track because because recursion adds calls to the stack
        """

        # if vertex is in visited, graph has been traversed
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            # Call dft for every neighbor in graph and pass in set of visited nodes
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            # Path list
            current_path = q.dequeue()
            # Current node is last item in path list
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.get_neighbors(current_node):
                    q.enqueue(current_path + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:
            current_path = s.pop()
            # current node were on is last node in path
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.vertices[current_node]:
                    # Make copy of current path
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # If path list is empty add starting node
        if len(path) == 0:
            path.append(starting_vertex)

        # If starting node is search node return path
        if starting_vertex == destination_vertex:
            return path

        # classify starting node as visited
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path + [neighbor])

                if result is not None:
                    return result


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
