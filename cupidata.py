graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [10],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}

def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == end:
            return path  # Return the path if the end vertex is reached
        for current_neighbour in graph_to_search[vertex]:
            if current_neighbour not in visited:
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
                visited.add(current_neighbour)
