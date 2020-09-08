from Graph import Graph

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)

graph.add_arc(1,2)
graph.add_arc(1,7)
graph.add_arc(1,3)
graph.add_arc(1,5)

graph.add_arc(2,5)
graph.add_arc(4,7)
graph.add_arc(6,5)
graph.add_arc(4,6)
graph.add_arc(7,5)
graph.add_arc(3,4)

graph.del_vertex(5)
graph.del_vertex(4)

graph.DFS(1)

print(str(graph))
print(graph.is_connected())