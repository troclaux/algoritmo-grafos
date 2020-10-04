from Graph import Graph

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)

graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(1,4)

""" graph.add_arrow(2,5)
graph.add_arrow(4,6)
graph.add_arrow(4,7)
graph.add_arrow(6,5)
graph.add_arrow(7,5)
graph.add_arrow(3,4) """

#graph.DFSS(1)
graph.is_hole_free()

print(str(graph))
print(graph.is_connected())