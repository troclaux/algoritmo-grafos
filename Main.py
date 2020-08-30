from Graph import Graph

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_arc(1,2)
graph.add_arc(1,3)
graph.add_arc(1,4)

print(str(graph))