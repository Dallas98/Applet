def search_path(graph, start, end):
    results = []
    generate_path(graph, [start], end, results)
    results.sort(key=lambda x: len(x))
    return results


def generate_path(graph, path, end, results):
    current = path[-1]
    if current == end:
        results.append(path)
    else:
        for n in graph[current]:
            if n not in path:
                generate_path(graph, path + [n], end, results)


def show_path(results):
    print('The path from', results[0][0], 'to', results[0][-1], 'is:')
    for path in results:
        print(path)


if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'],
             'B': ['E'],
             'C': ['D', 'F'],
             'D': ['B', 'E', 'G'],
             'E': ['D'],
             'F': ['D', 'G'],
             'G': ['E']}
    r1 = search_path(graph, 'A', 'D')
    show_path(r1)
