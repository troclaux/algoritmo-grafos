from Graph import Graph

graph = Graph()
neighbors = []

file = open('entrada.txt')

for line in file:
  line_without_enter = line.rstrip()
  separated_line = line_without_enter.split('=')
  graph.add_vertex(separated_line[0])
  neighbors.append(separated_line[1])

for vertex in graph.vertex_set:
  list_of_neighbors = neighbors[int(vertex)-1].split()
  for i in list_of_neighbors:
    graph.add_arrow(vertex, i)
  
#graph.DFSS(1)
print(graph)
graph.is_even_hole_free()