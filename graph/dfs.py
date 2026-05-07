class DFS:
    def __init__(self, graph, start):
        self.__start = start
        self.__graph = graph
        self.__stack = [self.__start]
        self.__prev_steps = {node: None for node in self.__graph}

    def start(self):
        while self.__stack:
            current = self.__stack.pop()
            for neighbor in self.__graph.get(current, []):
                self.__prev_steps[neighbor] = current
                self.__stack.append(neighbor)

    def get_path(self, target):
        path = []
        while target:
            path.append(target)
            target = self.__prev_steps.get(target)
        return path[::-1]

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

dfs = DFS(graph, 'A')
dfs.start()
path = dfs.get_path('F')
print(path)
