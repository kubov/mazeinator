import sys
from queue import Queue


class Edge(object):
    def __init__(self, weight, src=None, dst=None):
        self.weight = weight
        self.src = src
        self.dst = dst


class Vertex(object):
    def __init__(self):
        self.inputs = []
        self.outputs = []


class Graph(object):
    def __init__(self):
        self.edges = []
        self.vertices = []

    def add_node(self):
        self.vertices.append(Vertex())

    def connect(self, src, dst, weight):
        e = Edge(weight, src, dst)
        self.edges.append(e)
        src.outputs.append(dst)
        dst.inputs.append(src)

    def bfs(self, src=None, onnode=lambda x: x):
        if len(self.vertices) == 0:
            return None

        if src is None:
            src = self.vertices[0]

        q = Queue()

        for v in self.vertices:
            v.distance = sys.maxint
            v.parent = None

        src.distance = 0
        q.enqueue(src)

        while not q.empty():

            d = q.dequeue()
            onnode(d)
            for node in d.outputs:
                if node.distance == sys.maxint:
                    node.distance = d.distance + 1
                    node.parent = d
                    q.enqueue(node)


def pri(x):
    print x.distance
    print x.parent

if __name__ == "__main__":
    g = Graph()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.add_node()
    g.connect(g.vertices[0], g.vertices[1], 1)
    g.connect(g.vertices[1], g.vertices[2], 1)
    g.connect(g.vertices[0], g.vertices[3], 1)
    g.connect(g.vertices[2], g.vertices[4], 1)
    g.bfs(onnode=pri)
