from collections import deque


class BFS:
    def __init__(self, graph, start):
        self.__graph = graph
        self.__start = start
        self.__queue = deque([self.__start])
        self.__visted = set()
        self.__prev_setps = {node: None for node in self.__graph}

    def start(self):
        while self.__queue:
            current = self.__queue.popleft()
            for neighbor in self.__graph.get(current, []):
                if neighbor not in self.__visted:
                    self.__visted.add(neighbor)
                    self.__prev_setps[neighbor] = current
                    self.__queue.append(neighbor)

    def get_path(self, target):
        path = []
        while target:
            path.append(target)
            target = self.__prev_setps.get(target)
        return path[::-1]


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

bfs = BFS(graph, 'A')
bfs.start()
path = bfs.get_path('F')
print(path)
