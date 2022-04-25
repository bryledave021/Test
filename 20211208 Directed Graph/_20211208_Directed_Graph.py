#Unweighted Digraph figure imports-------------------
import networkx as nx
import matplotlib.pyplot as plt

#Unweighted Digraph-----------------------------------
class Digraph:
    def __init__ (self, edges):
        self.edges = edges
        self.Digraph_dict = {}
        for origin, destination in self.edges:
            if origin in self.Digraph_dict:
                self.Digraph_dict[origin].append(destination)
            else:
                self.Digraph_dict[origin] = [destination]

        print("The paths of travel: ", self.Digraph_dict)

    def get_paths(self, origin, destination, path =[]):
        path = path + [origin]

        if origin == destination:
            return [path]

        if origin not in self.Digraph_dict:
            return []
       
        paths = []

        for node in self.Digraph_dict[origin]:
            if node not in path:
                new_path = self.get_paths(node, destination, path)
                
                for p in new_path:
                    paths.append(p)

        return paths

    def shortest_path(self, origin, destination, path = []):
        path = path + [origin]

        if origin == destination:
            return path

        if origin not in self.Digraph_dict:
            return None

        shortest_path = None
        for node in self.Digraph_dict[origin]:
            if node not in path:
                shortestPath = self.shortest_path(node, destination, path)
                if shortestPath:
                    if shortest_path is None or len(shortestPath) < len(shortest_path): 
                        shortest_path = shortestPath


        return shortest_path

if __name__ == "__main__":
    routes = [
        ("TAGUIG","PATEROS"),
        ("PATEROS","PASIG"),
        ("PATEROS","MAKATI"),
        ("MAKATI","PASIG"),
        ("MAKATI","MUNTINLUPA"),
        ("PASIG","MARIKINA"),
        ("MAKATI", "MARIKINA"),
        ("MAKATI", "GUADALUPE"),
        ("MARIKINA", "MAKATI"),
        ]

    route_graph = Digraph(routes)

    origin = "TAGUIG"
    destination = "TAGUIG"
    print(f"the paths between {origin} and {destination}: ", route_graph.get_paths(origin, destination))
    print(f"Shortest path between {origin} and {destination}:", route_graph.shortest_path(origin, destination))
  
    
#----------------Unweighted Directed Graph Figure----------------------------

DigraphFig = nx.DiGraph()
DigraphFig.add_edges_from([("TG","PT"),("PT","PS"),("PT","MK"),("PS","MK"), ("PS","MRK"), ('MRK', 'MK'), ('MK', 'MN')])
pos = nx.spring_layout(DigraphFig)
nx.draw_networkx_nodes(DigraphFig, pos, node_size = 300)
nx.draw_networkx_edges(DigraphFig, pos, edgelist = DigraphFig.edges(), edge_color = "black")
nx.draw_networkx_labels(DigraphFig, pos)
plt.show()