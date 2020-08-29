class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = dict()

    def add_neighbor(self, v):
        if v.label in self.neighbors.keys():
            return f'{v.label} is already a neighbor of {self.label}'
        self.neighbors[v.label] = v

    def degree(self):
        return len(self.neighbors)

    def __str__(self):
        vertexDescription = f'\nId do vertice = {self.label}. Vizinhança: '
        for v in self.neighbors.keys():
            vertexDescription += f'{v} '
        vertexDescription += '\n'
        return vertexDescription
