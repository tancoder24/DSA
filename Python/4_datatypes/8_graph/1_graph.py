class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict_edge = {}
        for start, end in self.edges:
            if start in self.dict_edge:
                self.dict_edge[start].append(end)
            else:
                self.dict_edge[start] = [end]
    
    def get_path(self, start, end, path = []):

        path = path + [start]

        if start == end:
            return [path]
        if start not in self.dict_edge:
            return []

        paths = []
        for node in self.dict_edge[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.dict_edge:
            return None

        shortest_path = None
        for node in self.dict_edge[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    flight_routes = Graph(routes)
    print( flight_routes.dict_edge )

    print(flight_routes.get_shortest_path("Mumbai", "New York"))
