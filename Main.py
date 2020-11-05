from Graph import Graph

file = open('entrada.txt')
neighbors = []
j=0
number_of_vertices = 0

#conta numero de vertices para construir o grafo
for line in file:
  number_of_vertices = number_of_vertices + 1

#vai para o comeco do arquivo
file.seek(0)
#constroi o grafo
graph = Graph(number_of_vertices + 1)

#IMPORTANTE: para adicionar os vertices, a entrada precisa ter um '=' toda linha depois do vértice
#tambem é melhor adicionar os vertices de forma crescente
for line in file:
  line_without_enter = line.rstrip()
  separated_line = line_without_enter.split('=')
  #adiciona vertices ao grafo
  graph.add_vertex(int(separated_line[0]))
  #vincula vertices com seus vizinhos por meio de uma lista de adjacencia
  neighbors.append(separated_line[1])

#adiciona capacidades ao grafo
for vertex in graph.vertex_set:
  list_of_neighbors = neighbors[vertex-1].split()
  for i, value in enumerate(list_of_neighbors):
    value = int(value)
    if((i%2) == 0):
      graph.add_arrow(vertex, value)
      j=int(value)
    else:
      graph.capacities[int(vertex)][j] = value

print(graph)
#print('numero de vertices no grafo: ', len(graph.vertex_set))

#ford fulkerson recebe como parametros respectivamente (origem, destino)
print('o fluxo maximo desse grafo eh: ', str(graph.ford_fulkerson(1, 7)))
