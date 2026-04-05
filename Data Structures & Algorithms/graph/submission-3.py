class Graph:
    
    def __init__(self):
        self.dgraph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.dgraph:
            self.dgraph[src] = []
        if dst not in self.dgraph:
            self.dgraph[dst] = []
        self.dgraph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.dgraph:
            return False
        for i in range(len(self.dgraph[src])):
            if self.dgraph[src][i] == dst:
                self.dgraph[src].pop(i)
                return True
        return False

    def hasPath(self, src: int, dst: int, visited = None) -> bool:
        if not visited:
            visited = set()
        if src not in self.dgraph:
            return False
        
        if src in visited:
            return False
        visited.add(src)

        for neighbor in self.dgraph[src]:
            if neighbor == dst:
                return True
            if self.hasPath(neighbor,dst,visited):
                return True
        return False