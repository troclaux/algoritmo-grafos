from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertex_set = dict()

    def add_vertex(self, label):
        if label not in self.vertex_set.keys():
            self.vertex_set[label] = []
        else:
            return f'{label} already exists in this graph.'

    def add_arc(self, label1, label2):
        v1 = self.vertex_set[label1]
        v2 = self.vertex_set[label2]

        v1.add_neighbor(v2)

    def add_edge(self, label1, label2):
        v1 = self.vertex_set[label1]
        v2 = self.vertex_set[label2]

        v1.add_neighbor(v2)
        v2.add_neighbor(v1)

    def del_vertex(self, label):
        v = self.vertex_set[label]
        v.pop(label)
        
    """ def compact(self):
        set = self.vertex_set
        for i in range(0, len(set) + 1):
            save = i
            while set.get(i) is None:
                if i <= len(set):
                    i += 1
            set.get(i)
 """
    def max_degree(self):
        max_deg = 0

        for v in self.vertex_set.values():
            max_deg = max(max_deg, len(v.neighbors))

        return max_deg

    def is_undirected(self):
        for v in self.vertex_set.values():
            for u in v.neighbors.values():
                if v not in u.neighbors.values():
                    return False
        return True

    def subjacent(self):
        subj = Graph()

        for v in self.vertex_set.keys():
            subj.add_vertex(v)

        for v in self.vertex_set.values():
            for u in v.neighbors.values():
                v_subj = subj.vertex_set[v.label]
                u_subj = subj.vertex_set[u.label]

                v_subj.add_neighbor(u_subj)
                u_subj.add_neighbor(v_subj)

        return subj

    def is_connected(self):
        # TODO
        pass

    """ def BFS(self, id):
        for vertex in self.vertex_set
            
        # TODO
        pass """

    def __str__(self):
        graphDescription = '\n' + f'Grafo, grau máximo {self.max_degree()} '
        if self.is_undirected():
            graphDescription += 'Não direcionado\n'
        else:
            graphDescription += 'Direcionado\n'

        for v in self.vertex_set.values():
            graphDescription += v.__str__()

        return graphDescription
