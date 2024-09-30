class Graph:
    def __init__(self, edges):
        self.edges = edges



if __name__ == '__main__':
    routes = [
        ("paris", 'madrid'),
        ('marseille', 'turin')
    ]

    graph = Graph(routes)
    print(graph)
   