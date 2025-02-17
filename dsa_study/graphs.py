class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []
            return True
        return False

    def remove_vertex(self, node):
        if node in self.adj_list:
            for other_node in self.adj_list[node]:
                self.adj_list[other_node].remove(node)
            del self.adj_list[node]
            return True
        return False

    def add_edge(self, node1, node2, weight = 1):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)
            return True
        return False

    def remove_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            if node2 in self.adj_list[node1] and node1 in self.adj_list[node2]:
                self.adj_list[node1].remove(node2)
                self.adj_list[node2].remove(node1)
                return True
            else:
                return False
        return False

graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
print(graph.adj_list)
graph.remove_edge('a', 'c')
print(graph.adj_list)
graph.remove_vertex('b')
print(graph.adj_list)
