# coding: utf-8
#!python
# graph.py
# By Timofey Makhlay (github.com/timomak/)

class ArrayVertex(object):
    def __init__(self, data, champ):
        """
        Initialize the Vertex with the given data.
        Running: O(1)
        """
        self.data = data
        self.champ = champ
        self.edges = []

    def __repr__(self):
        """Return a string represenation of this Vertex"""
        return 'Vertex({!r})'.format(self.data)

    def get_neighbors(self):
        """
        Return Array with all the neightbors.
        Runtime: O(n)
        """
        neighbors = []
        for tuple in self.edges:
            neighbors.append(tuple[0])
        return neighbors

class ArrayGraph(object):
    def __init__(self, iterable=None):
        """
        Initialize this Array Graph and append the given items, if any.
        Runtime: O(1) if no items. O(items) with items.
        """
        self.vertices = []
        self.size = 0

        # Add vertices if provided.
        if iterable is not None:
            for item in iterable:
                self.addVertex(item)

    def __repr__(self):
        """Return a string representation of this graph."""
        return 'Graph({!r})'.format(self.getVertices())

    def addVertex(self, vert):
        """
        Adds an instance of Vertex to the graph.
        Runtime: O(n)
        """
        if self.getVertex(vertKey=vert) != None:
            raise ValueError("Vertex with this key already exists.")

        if vert.key_:
            # print("Has key")
            new_vert = ArrayVertex(vert.key_, vert)
        else:
            new_vert = ArrayVertex(vert)
        self.vertices.append(new_vert)
        self.size += 1

    def addEdge(self, fromVert, toVert, weight=1):
        """
        Adds a new, weighted, directed edge to the graph that connects two vertices.
        Runtime: O(number of vertices) + O(number of edges in fromVert)
        """
        if fromVert == toVert:
            raise ValueError("Can't create an edge with the same Vertex.")

        start = None
        end = None

        counter = 0

        for vert in self.vertices: # O(n)
            if vert.data == fromVert:
                start = counter
            elif vert.data == toVert:
                end = counter
            counter += 1

        if start == None:
            raise ValueError(fromVert, " is not a Vertex.")
        if end == None:
            raise ValueError(toVert, " is not a Vertex.")

        try:
            weight = int(weight)
        except ValueError:
            raise ValueError("The weight has to be an integer.")


        can_append = True
        for edge in self.vertices[start].edges: # O(n)
            if edge == (self.vertices[end], weight):
                # Already has this edge
                can_append = False
                # raise ValueError("The Edge already exists")

        if can_append == True:
            self.vertices[start].edges.append((self.vertices[end], weight))


    def getVertex(self, vertKey):
        """
        Finds the vertex in the graph named vertKey.
        Runtime: O(n) for vertices.
        """
        for vert in self.vertices: # O(n)
            if vert.data == vertKey:
                return vert
        return None

        raise ValueError("The vertex doesn't exist.")

    def getVertices(self):
        """
        Returns the list of all vertices in the graph.
        Runtime: O(1)
        """
        return self.vertices


    def getNeighbors(self, x):
        """
        Lists all vertices y such that there is an edge from the vertex x to the vertex y.
        Running: O(n) because of getVertex()
        """
        current_vert = self.getVertex(x)

        return current_vert.edges

    def find_path(self, start_vertex, end_vertex, path=None):
        """
        Setup for the find path function to work properly.
        Running: O(n^3)
        """
        if path == None: # Empty path start.
            path = []

        # Check if the Vertices are in the graph.
        start_vertex = self.getVertex(start_vertex)
        end_vertex = self.getVertex(end_vertex)

        # Run recursive function to find a path.
        return self._find_path_recursive(start_vertex, end_vertex, path)

    def _find_path_recursive(self, current_vertex, end_vertex, path=None):
        """
        Find a path from start_vertex to end_vertex in graph.
        Recursive loop.
        Runtime: O(n^3)
        Resources: https://www.python-course.eu/graphs_python.php
        """
        # Set the given current vertex as the last vertex on the path.
        path = path + [current_vertex]

        # If the current Vertex is the end vertex, we found the path.
        if current_vertex.data == end_vertex.data:
            return path

        for (vertex, weight) in current_vertex.edges: # For every neighboring Vertex to the current vertex. O(n)
            if vertex not in path: # If we haven't checked the neighbor's neighbors. O(n)
                extended_path = self._find_path_recursive(vertex, end_vertex, path) # Continue checking the neightbor's neightbors. O(n)
                if extended_path:
                    return extended_path
        return None

    def breadth_first_search(self, vertex, n = 0):
        """
        Find all neightboring nodes n edges away from the provided vertex.
        Running: O(n^2)
        """
        explored = [] # All the neighbors

        start = self.getVertex(vertex) # Checking if the start Vertex is in the graph. O(n)

        queue = [] # Queue to track the current Vertex we're exploring.

        queue.append(start) # O(1)

        counter = 0 # To stop at the right depth.

        while queue: # While not Empty. O(m)
            vert = queue.pop(0) # Dequeue the first in queue.O(m)

            if vert not in explored: # If it wasn't already explored. O(x)
                explored.append(vert) # Add it to explored. O(1)
                edges = vert.edges # Add it's neighbors to the queue. O(1)

                for edge in edges:
                    queue.append(edge[0]) # Because we have tuples (Vertex('1'), weight).
            counter += 1
            if counter == n and n > 0:
                return explored
        return explored

    def find_shortest_path(self, start_vert, end_vert):
        """
        Returns the Vertices that form the path from the start to the end vertex using BFS.
        Runnning: O(n^3)
        Resources: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        Thanks Vincenzo for telling me that the first BFS path found is the fastest path.
        """
        # Checking if the vertices are in the graph.
        start = self.getVertex(start_vert) # O(n)
        end = self.getVertex(end_vert) # O(n)

        queue = [(start, [start])] # (Vertex, [path from first to current vertex])

        while queue: # While not Empty. O(m)
            (vertex, path) = queue.pop(0) # Dequeue the first in queue. O(m)

            for next in set(vertex.get_neighbors()) - set(path): # Next is one of the neightbors of the vertex that aren't in the path already. O(n^2)
                if next == end: # If found
                    return path + [next] # Return the current path + the current iterating vertex.
                else: # If not found
                    queue.append((next, path + [next])) # Add the current vertex and the path it took to get to it so far.
        return None

    def depth_first_search(self, start):
        """
        DFS (Depth First Search) function on graph. Start is the "root" vertex.
        Runtime: O(m) + O(n^3)
        Resources: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        """
        start = self.getVertex(start) # O(n)
        return [i for i in self.depth_first_search_recursive(start)] # O(m) + O(n^3)


    def depth_first_search_recursive(self, start, visited=None):
        """
        DFS (Depth First Search) recursive loop. Start is the "root" vertex.
        Runtime: O(n^3)
        Resources: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        """
        if visited is None:
            visited = set()
        visited.add(start) # O(1)
        for next in set(start.get_neighbors()) - visited: # neighbors that haven't been visited. O(n^2)
            # print("Visited Before:", visited, next)
            self.depth_first_search_recursive(next,visited) # O(n)
            # print("Visited After:", visited)
        return visited

    def dijkstra(self, start, end):
        """
        Finding the most cost effective path using Dijkstra's algorithm.
        Runtime: O(n^2)
        Resources: https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
        """
        start = self.getVertex(start) # O(n)
        end = self.getVertex(end) # O(n)

        vertices = self.getVertices().copy() # Copy Array of all the vertices. O(n)

        distances = { vertex : float('inf') for vertex in vertices } # { Vertex(n) : infinite } Distance from start to the vertex. O(n)
        previous_vertices = { vertex : None for vertex in vertices } # { Vertex (n) : None } Lowest cost neightbor to get to start from vertex. O(n)

        distances[start] = 0 # Setting the weight of root to 0. O(1)

        while vertices: # While Vertices isn't empty O(n)

            current_vertex = min(vertices, key=lambda vertex: distances[vertex]) # The lowest weight (I think)

            vertices.remove(current_vertex) # Won't iterate over itself. O(1)

            if distances[current_vertex] == float('inf'):
                break # Something probably went wrong.

            for neighbour, cost in current_vertex.edges: # For vertex, weight in neightbors of current vertex. edges = [(Vertex(n), weight)] O(n)
            # MARK: neighbor could cause issues if it's not a string. (You could change it to data instead of Vertex object.)
                alternative_route = distances[current_vertex] + cost # check the cost of passing through to the neightbor from current vertex.

                if alternative_route < distances[neighbour]: # If the cost is lower than the already set weight...
                    distances[neighbour] = alternative_route # Update the cost with the current weight
                    previous_vertices[neighbour] = current_vertex # Keep track of the current vertex because it can access the neightbor at a low cost.

        path = [] # Queue
        current_vertex = end # Starting to look for a path, from the "end" vertex.
        weight = distances[end]

        while previous_vertices[current_vertex] is not None: # If the current vertex has neightbors
            path.insert(0, current_vertex) # Add the current vertex to the left of the queue
            current_vertex = previous_vertices[current_vertex] # Set the next item in the path.

        if path: # If there's any path found
            path.insert(0, current_vertex) # Add the "start" vertex as the first in queue (or the first vertex to access the "end" vertex)
        return path, weight

    def clique(self, vert):
        """
        Start with an arbitrary vertex u and add it to the clique

        For v in remaining vertices not in the clique
        If v is adjacent to every other vertex already in the clique.
        	Add v to the clique
        	Discard v otherwise
        Runtime: O(n^3)
        """
        start = self.getVertex(vert) # Root

        vertices = set(self.getVertices())

        clique = set()
        clique.add(start)

        for vertex in vertices - clique:
            neighbor_of_all = True
            for v in clique:
                if vertex not in v.get_neighbors():
                    # print("Vertex {} and Vertex {} are not neighbors".format(vertex, v))
                    neighbor_of_all = False
            if neighbor_of_all == True:
                clique.add(vertex)

        return list(clique)

    def find_all_champs_same_class_as(self, vert):
        """
        Find all champs for each champ class in vert.champ
        Runtime: O(3) * O(51) * (O(3) + O(3) + (O(5) * O(7)) = O(6273)
        """
        start = self.getVertex(vert) # Root

        checked_classes = set()
        array_of_champs = {} # { 'yordle': set('kennen', ...), ...}

        # print("All of {}'s classes: {}".format(vert, start.champ.classes))

        for class_ in start.champ.classes: # O(3) Worst Case
            if class_ != None:
                # print("Checking {} class".format(class_))
                vertices = set(self.getVertices())

                clique = set()
                clique.add(start)

                for vertex in vertices - clique: # O(51) Worst
                    # print("Comparing {} to {}".format(vert, vertex))
                    if class_ in vertex.champ.classes: # O(3) Worse
                        matching_classes = set(start.champ.classes).intersection(set(vertex.champ.classes))
                        has_unchecked_match = False

                        for match in matching_classes: # O(3) Worse
                            if match not in checked_classes:
                                has_unchecked_match = True
                                # print("{} matches to {} by {} class".format(vertex, vert, match))

                        if has_unchecked_match == True:
                            neighbor_of_all = True
                            for v in clique: # O(5) Worse
                                if vertex not in v.get_neighbors(): # O(7) Worse
                                    # print("Vertex {} and Vertex {} are not neighbors".format(vertex, v))
                                    neighbor_of_all = False
                            if neighbor_of_all == True:
                                clique.add(vertex)
                    # else:
                    #     break

                array_of_champs[class_] = clique # O(1)
        return array_of_champs
