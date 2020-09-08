class Graph:
    def __init__(self):
        self.vertex_set = dict()

    def add_vertex(self, label):
        if label not in self.vertex_set.keys():
            self.vertex_set[label] = []
        else:
            return f'{label} already exists in this graph.'

    def add_arc(self, label1, label2):
        if label1 not in self.vertex_set or label2 not in self.vertex_set:
            print('Erro: um dos vértices não existe no grafo')
        elif  label2 in self.vertex_set[label1]:
            print('Arco ' + str(label1) + ' -> ' + str(label2) + ' já existe')
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
        
   """  def compact(self):
        for i in self.vertex_set.keys():
            save = i

            while i not in self.vertex_set.keys():
                i += 1
            print('expressao: ' + str(len(self.vertex_set) - i))
            
            for j in range(len(self.vertex_set) - i):
                newId = save + j
                oldId = i + j
                print('j: ', j)
                print('newId: ' + str(newId))
                print('oldId: ' + str(oldId))
                self.vertex_set[newId] = self.vertex_set.pop(oldId)
            i = save
        return self """


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
        graphDescription = '\n' + f'Grafo, grau máximo {self.max_degree()} '
        if self.is_undirected():
            graphDescription += 'Não direcionado\n'
        else:
            graphDescription += 'Direcionado\n'

        
        for v in self.vertex_set.keys():
            graphDescription += 'Vértice: ' + str(v) + ', vizinhança:' + str(self.vertex_set[v]) + '\n'

        return graphDescription
