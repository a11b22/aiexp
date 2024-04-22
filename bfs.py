visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        print("Visited nodes:", visited)
        print("Queue:", queue)
        print("Current node:", current_node)

        if current_node in graph:
            for neighbour in graph[current_node]:
                if neighbour not in visited and neighbour not in queue:
                    visited.append(neighbour)
                    queue.append(neighbour)

        print("-----")

        print(current_node, end=" ")

graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbours = input("Enter its neighbours separated by spaces: ").split()
    graph[node] = neighbours

# Driver Code
start_node = input("Enter the starting node: ")
print("Following is the Breadth-First Search:")
bfs(visited, graph, start_node)
