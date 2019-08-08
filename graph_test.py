from graph import ArrayGraph, ArrayVertex
import unittest

class ArrayVertexTest(unittest.TestCase):
    def test_init(self):
        data = "A"
        vertex = ArrayVertex(data)
        assert vertex.data is data

class ArrayGraphTest(unittest.TestCase):
    def test_empty_init(self):
        vertices = []
        graph = ArrayGraph()
        assert graph.size is 0
        assert graph.vertices == []

    def test_iterable_init(self):
        vertices = [1,2,3,4]
        graph = ArrayGraph(vertices)
        assert graph.size is 4
        assert len(graph.vertices) is 4

    def test_addVertex(self):
        vertices = []
        graph = ArrayGraph()
        graph.addVertex("1")
        graph.addVertex("2")
        assert graph.size is 2
        assert len(graph.vertices) == 2

    def test_addVertex_duplicate(self):
        vertices = []
        graph = ArrayGraph()
        graph.addVertex("1")
        assert graph.size is 1
        with self.assertRaises(ValueError): # Can't add if already present.
            graph.addVertex("1")
        assert len(graph.vertices) is 1

    def test_addEdge(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2,3)
        graph.addEdge(2,3,1)
        assert len(graph.vertices[0].edges) is 1
        assert len(graph.vertices[1].edges) is 1
        assert len(graph.vertices[2].edges) is 0
        assert graph.vertices[0].edges[0] == (graph.vertices[1], 3)
        assert graph.vertices[1].edges[0] == (graph.vertices[2], 1)

    def test_addEdge_to_itself(self):
        vertices = [1]
        graph = ArrayGraph(vertices)
        with self.assertRaises(ValueError):
            graph.addEdge(1,1)

    def test_addEdge_to_non_existant_vertex(self):
        vertices = [1,2]
        graph = ArrayGraph(vertices)
        with self.assertRaises(ValueError):
            graph.addEdge(1,3)
        with self.assertRaises(ValueError):
            graph.addEdge(2,3)
        graph.addEdge(1,2)

        assert len(graph.vertices) is 2
        assert len(graph.vertices[0].edges) is 1
        assert graph.vertices[0].edges[0] == (graph.vertices[1], 0)

    def test_getVertex(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        assert len(graph.vertices) is 3
        assert graph.size is 3
        assert graph.getVertex(2) == graph.vertices[1]

    def test_getVertex_not_found(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        assert len(graph.vertices) is 3
        assert graph.size is 3
        assert graph.getVertex(2) == graph.vertices[1]
        assert graph.getVertex(4) == None

    def test_getVertices(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        assert len(graph.vertices) is 3
        assert graph.getVertices() == graph.vertices

    def test_get_neighbors(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2,3)
        graph.addEdge(2,3,1)
        assert graph.size is 3
        assert graph.vertices[0].edges[0] == (graph.vertices[1], 3)
        assert graph.getNeighbors(1) == [(graph.vertices[1], 3)]

    def test_find_path(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2,3)
        graph.addEdge(2,3,1)
        assert graph.find_path(1, 3) == [graph.vertices[0],graph.vertices[1],graph.vertices[2]]

    def test_find_path_broken(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2)
        graph.addEdge(2,3,1)
        assert graph.find_path(1, 3) == [graph.vertices[0],graph.vertices[1],graph.vertices[2]]
        with self.assertRaises(ValueError):
            graph.addEdge(3,4)

    def test_breadth_first_search(self):
        vertices = [1,2,3]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2)
        graph.addEdge(2,3)
        assert graph.breadth_first_search(1) == [graph.vertices[0], graph.vertices[1], graph.vertices[2]]

    def test_find_shortest_path(self):
        vertices = [1,2,3,4,5]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2)
        graph.addEdge(1,4)
        graph.addEdge(2,3)
        graph.addEdge(2,4)
        graph.addEdge(2,5)
        graph.addEdge(3,5)
        path = graph.find_shortest_path(1, 5)
        assert path == [graph.vertices[0], graph.vertices[1], graph.vertices[4]]
        assert len(path) == 3

    def test_depth_first_search(self):
        vertices = [1,2,3,4,5]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2,4)
        graph.addEdge(1,4,5)
        graph.addEdge(2,3,6)
        graph.addEdge(2,4,9)
        graph.addEdge(2,5,6)
        graph.addEdge(3,5,10)
        path = graph.depth_first_search(1)
        assert len(path) == 5 # It's a dictionary, so it's hard to test the contents of it.

    def test_dijkstra(self):
        vertices = [1,2,3,4,5]
        graph = ArrayGraph(vertices)
        graph.addEdge(1,2,4)
        graph.addEdge(1,4,5)
        graph.addEdge(2,3,6)
        graph.addEdge(2,4,9)
        graph.addEdge(2,5,6)
        graph.addEdge(3,5,10)
        path, weight = graph.dijkstra(1,5)
        assert len(path) == 3
        assert weight == 10

    def test_clique(self):
        graph = ArrayGraph([1,2,3,4])
        graph.addEdge(1,2)
        graph.addEdge(1,3)
        graph.addEdge(2,3)
        graph.addEdge(3,4)
        assert len(graph.clique(1)) == 3
        assert graph.vertices[0] in graph.clique(1)
        assert graph.vertices[1] in graph.clique(1)
        assert graph.vertices[2] in graph.clique(1)
        assert graph.vertices[3] not in graph.clique(1)
