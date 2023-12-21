class Vertex:
    def __init__(self, key):
        self.id = key

        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " connected To: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}

        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1

        newVertex = Vertex(key)

        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]

        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)

        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    # This is the overload built-in function to print the Graph object to a string

    # It outputs all nodes (Vertex class) in the Graph object to the string

    # For example,  there are three nodes in the graph.

    # the output is as follows.

    # 0 connected To: [1,2],1 connected To: [2],2 connected To: [0]

    # If the node is None, then it outputs "None"

    # Please also note that the answer is case sensitive and space sensitive as well. No mark will be awarded if answers in the test cases are not matched,

    # Please write your code here

    def __str__(self):
        if not self.vertList:
            return "None"

        return ",".join(str(self.vertList[vertex]) for vertex in self.getVertices())
