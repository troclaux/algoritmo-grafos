from Graph import Graph

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_arc(1,2)
graph.add_arc(1,2)
graph.add_arc(2,1)
graph.add_arc(5,2)
graph.add_arc(1,3)
graph.add_arc(1,4)
graph.add_edge(1,3)

print(str(graph))