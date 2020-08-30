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
        if label1 in self.vertex_set and label2 in self.vertex_set:
            self.vertex_set[label1].append(label2)
        else:
            print('Erro: um dos vértices não existe no grafo')

    def add_edge(self, label1, label2):
        if label1 in self.vertex_set and label2 in self.vertex_set:
            self.vertex_set[label1].append(label2)
            self.vertex_set[label2].append(label1)
        else:
            print('Erro: um dos vértices não existe no grafo')

    def del_vertex(self, label):
        self.vertex_set.pop(label)
        
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

        for v in self.vertex_set.keys():
            max_deg = max(max_deg, len(self.vertex_set[v]))

        return max_deg

    def is_undirected(self):
        for v in self.vertex_set.keys():
            for u in self.vertex_set[v]:
                if v not in self.vertex_set[u]:
                    return False
        return True

    def subjacent(self):
        subj = Graph()

        for v in self.vertex_set.keys():
            subj.add_vertex(v)

        for v in self.vertex_set.values():
            for u in self.vertex_set[v]:

                subj.vertex_set[u].append(v)
                #v_subj = subj.vertex_set[v.label]
                #u_subj = subj.vertex_set[u.label]

                #v_subj.add_neighbor(u_subj)
                #u_subj.add_neighbor(v_subj)
                #consertar bugs em caso de repeticao de valores no dicionario

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

        
        for v in self.vertex_set.keys():
            graphDescription += 'Vértice: ' + str(v) + ', vizinhança:' + str(self.vertex_set[v]) + '\n'

        return graphDescription
