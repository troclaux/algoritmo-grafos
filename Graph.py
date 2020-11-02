class Graph:
    def __init__(self, vertex_set_size):
        self.vertex_set = dict()
        self.time = 0
        self.discovery_time = []
        self.finishing_time = []
        self.parents = []
        self.visited = set()
        self.not_in_hole = []
        self.in_path = []

        self.capacities = [[0 for x in range(vertex_set_size)] for y in range(vertex_set_size)]
        self.flows = [[0 for x in range(vertex_set_size)] for y in range(vertex_set_size)]

    def add_vertex(self, label):
        if label not in self.vertex_set.keys():
            self.vertex_set[label] = []
        else:
            return f'{label} already exists in this graph.'

    def add_arrow(self, label1, label2):
        if label1 not in self.vertex_set or label2 not in self.vertex_set:
            print('Erro: um dos vértices não existe no grafo')
        elif  label2 in self.vertex_set[label1]:
            print('Seta ' + str(label1) + ' -> ' + str(label2) + ' já existe')
        else:
            self.vertex_set[label1].append(label2)
            self.vertex_set[label1].sort()

    def add_edge(self, label1, label2):
        if label1 not in self.vertex_set or label2 not in self.vertex_set:
            print('Erro: um dos vértices não existe no grafo')
        elif label1 in self.vertex_set[2] and label2 in self.vertex_set[1]:
            print('Aresta ' + str(label1) + ' <-> ' + str(label2) + ' já existe')
        else:
            if label1 not in self.vertex_set[label2]:
                self.vertex_set[label2].append(label1)
                self.vertex_set[label2].sort()
            if label2 not in self.vertex_set[label1]:
                self.vertex_set[label1].append(label2)
                self.vertex_set[label1].sort()

    def del_vertex(self, label):
        self.vertex_set.pop(label)
        for v in self.vertex_set:
            if label in self.vertex_set[v]:
                self.vertex_set[v].remove(label)

    #def compact(self):

    def ford_fulkerson(self, source, sink):
        residual_graph = self.generate_residual_graph()
        max_flow = 0
        path_flow = 999
        augmenting_path = []
        #nao sei como determinar augmenting_path
        #enquanto tiver caminho aumentante
        while( self.BFS_ford(source, sink, augmenting_path) ):
            while(sink is not source):
                path_flow = min(path_flow, self.graph)
            max_flow = max_flow + path_flow
            #porque declarar v?
            v = sink
            while(v is not source):
                u = augmenting_path[v]
                self.capacities[u][v] -= path_flow
                self.capacities[v][u] += path_flow
                v = augmenting_path[v]
            
        return max_flow

    def BFS_ford(self, s, t, augmenting_path):
        queue = [s]
        visited = [s]
        while(queue):
            u = queue.pop(0)
            for neighbor in self.vertex_set[u]:
                if neighbor not in visited and self.capacities[u][neighbor] > 0:
                    print(' ' + str(u) + ' -> ' + str(neighbor))
                    queue.append(neighbor)
                    visited.append(neighbor)
                    augmenting_path[neighbor] = u
        if t in visited:
            return True
        else:
            print('busca em largura concluida')
            return False

    def generate_residual_graph(self):
        residual_graph = self
        for parent in residual_graph.vertex_set:
            for child in residual_graph.vertex_set[parent]:
                residual_graph.capacities[parent][child] = self.capacities[parent][child] - self.flows[parent][child]
        return residual_graph


    def set_capacity(self, parent, child, capacity):
        if child in self.vertex_set[parent]:
            self.capacities[parent][child] = capacity
        else:
            print('vertice ' + child + ' nao é vizinho de ' + parent)

    def set_flow(self, parent, child, flow):
        if child in self.vertex_set[parent]:
            self.flows[parent][child] = flow
        else:
            print('vertice ' + child + ' nao é vizinho de ' + parent)

    def max_degree(self):
        max_deg = 0

        for v in self.vertex_set.keys():
            max_deg = max(max_deg, len(self.vertex_set[v]))

        return max_deg

    def degree(self, label):
        return len(self.vertex_set[label])

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

        return subj

    def DFS(self, id):
        print('DFS :\n')
        for vertex in self.vertex_set:
            self.discovery_time.insert(vertex, -1)
            self.finishing_time.insert(vertex, -1)
        self.discovery_time[1] = 1
        for vertex in self.vertex_set:
            if self.discovery_time[vertex] == -1:
                self.DFS_visit(vertex)

    def DFS_visit(self, id):
        self.time = self.time + 1
        self.discovery_time.insert(id, self.time)
        for vertex in self.vertex_set[id]:
            if self.discovery_time[vertex] == -1:
                print(str(id) + ' -> ' + str(vertex))
                self.parents.insert(vertex, id)
                self.DFS_visit(vertex)
        self.time += 1
        self.finishing_time.insert(id, self.time)

    def DFSS(self, id):
        if id not in self.visited:
            print(str(id))
            self.visited.add(id)
            for neighbor in self.vertex_set[id]:
                self.DFSS(neighbor)

    def is_even_hole_free(self):
        size = 1 + len(self.vertex_set)
        self.not_in_hole =  [[[0] * size] *size] *size
        self.in_path = [0] * size

        for u in self.vertex_set:
            self.in_path[int(u)] = 1
            for v in self.vertex_set:
                for w in self.vertex_set[v]:
                    if u in self.vertex_set[v] and u not in self.vertex_set[w]:
                        if self.not_in_hole[int(u)][int(v)][int(w)] == 0:
                            self.in_path[int(v)] = 1
                            if not self.process(u,v,w):
                                return False
                            self.in_path[int(v)] = 0
            self.in_path[int(u)] = 0
        print('graph does not contain a hole')
        #if len(cycle.vertex_set) % 2 == 1 and len(cycle.vertex_set<6):
            #print('graph is even-hole-free')
            #return True

    def process(self, a, b, c):
        self.in_path[int(c)] = 1
        for d in self.vertex_set[c]:
            if d not in self.vertex_set[a] and d not in self.vertex_set[b]:
                # then abcd is P4 of G
                if self.in_path[int(d)] == 1:
                    print('Graph has a hole')
                    return False
                elif self.not_in_hole[int(b)][int(c)][int(d)] == 0:
                    self.process(b,c,d)
        self.in_path[int(c)] = 0
        self.not_in_hole[int(a)][int(b)][int(c)] = 1
        self.not_in_hole[int(c)][int(b)][int(a)] = 1

        return True



    def BFS(self, id):
        #print('executando BFS:\n')
        queue = [id]
        visited = [id]
        while(queue):
            id = queue.pop(0)
            for neighbor in self.vertex_set[id]:
                if neighbor not in visited:
                    print(' ' + str(id) + ' -> ' + str(neighbor))
                    queue.append(neighbor)
                    visited.append(neighbor)

    def is_connected(self):
        for id in self.vertex_set:
            queue = [id]
            visited = [id]
            while(queue):
                id = queue.pop(0)
                for neighbor in self.vertex_set[id]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.append(neighbor)
            if len(visited) < len(self.vertex_set):
                return False
        return True

    def __str__(self):
        graphDescription = '\n' + f'Grafo de grau máximo {self.max_degree()} '
        if self.is_undirected():
            graphDescription += 'não direcionado\n\n'
        else:
            graphDescription += 'direcionado\n\n'


        for v in self.vertex_set.keys():
            list_of_capacities = []
            for i in self.capacities[int(v)]:
                if i != 0:
                    list_of_capacities.append(i)
            graphDescription += 'Vértice: ' + str(v) + ', vizinhança:' + str(self.vertex_set[v]) + ', capacidades: ' + str(list_of_capacities) + '\n'

        return graphDescription
