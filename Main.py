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

#adiciona vertices ao grafo
for line in file:
  line_without_enter = line.rstrip()
  separated_line = line_without_enter.split('=')
  graph.add_vertex(separated_line[0])
  neighbors.append(separated_line[1])

#adiciona capacidades ao grafo
for vertex in graph.vertex_set:
  list_of_neighbors = neighbors[int(vertex)-1].split()
  for i, value in enumerate(list_of_neighbors):
    if((i%2) == 0):
      graph.add_arrow(vertex, value)
      j=int(value)
    else:
      graph.capacities[int(vertex)][j] = value
  
print(graph)