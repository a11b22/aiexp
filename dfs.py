def dfs(visited, graph, node, path=[]):  # Function for DFS
    print("Visiting node:", node)
    visited.add(node)
    path.append(node)
    print("Visited nodes:", path)

    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            dfs(visited, graph, neighbour, path)


    path.pop()

graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbours = input("Enter its neighbours separated by spaces: ").split()
    graph[node] = neighbours

start_node = input("Enter the start node: ")
print("Following is the DFS:")
dfs(set(), graph, start_node)
            
