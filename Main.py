from Graph import Graph

neighbors = []
j=0
number_of_vertices = 0
file = open('entrada.txt')

graph = Graph(10)

for line in file:
  number_of_vertices = number_of_vertices + 1
  line_without_enter = line.rstrip()
  separated_line = line_without_enter.split('=')
  graph.add_vertex(separated_line[0])
  neighbors.append(separated_line[1])


for vertex in graph.vertex_set:
  list_of_neighbors = neighbors[int(vertex)-1].split()
  for i, value in enumerate(list_of_neighbors):
    print("i: " + str(i) + " value:" + str(value))
    if((i%2) == 0):
      graph.add_arrow(vertex, value)
      j=value
    else:
      graph.capacities[int(vertex)][0] = value
  

#graph.DFSS(1)
print(graph)
print(graph.capacities)
graph.is_even_hole_free()