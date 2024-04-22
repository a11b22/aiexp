import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth, graph):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        left_child_index = nodeIndex * 2
        right_child_index = nodeIndex * 2 + 1
        graph[str(scores[nodeIndex])] = [str(scores[left_child_index]), str(scores[right_child_index])]
        return max(minimax(curDepth + 1, left_child_index, False, scores, targetDepth, graph),
                   minimax(curDepth + 1, right_child_index, False, scores, targetDepth, graph))
    else:
        left_child_index = nodeIndex * 2
        right_child_index = nodeIndex * 2 + 1
        graph[str(scores[nodeIndex])] = [str(scores[left_child_index]), str(scores[right_child_index])]
        return min(minimax(curDepth + 1, left_child_index, True, scores, targetDepth, graph),
                   minimax(curDepth + 1, right_child_index, True, scores, targetDepth, graph))

# Function to construct graph
def construct_graph(curDepth, nodeIndex, maxTurn, scores, targetDepth, graph):
    if curDepth == targetDepth:
        return

    if maxTurn:
        left_child_index = nodeIndex * 2
        right_child_index = nodeIndex * 2 + 1
        graph[str(scores[nodeIndex])] = [str(scores[left_child_index]), str(scores[right_child_index])]
        construct_graph(curDepth + 1, left_child_index, False, scores, targetDepth, graph)
        construct_graph(curDepth + 1, right_child_index, False, scores, targetDepth, graph)
    else:
        left_child_index = nodeIndex * 2
        right_child_index = nodeIndex * 2 + 1
        graph[str(scores[nodeIndex])] = [str(scores[left_child_index]), str(scores[right_child_index])]
        construct_graph(curDepth + 1, left_child_index, True, scores, targetDepth, graph)
        construct_graph(curDepth + 1, right_child_index, True, scores, targetDepth, graph)

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)

graph = {}
optimal_solution = minimax(0, 0, True, scores, treeDepth, graph)

print("Optimal solution:", optimal_solution)
print("Graph:")
print(graph)
        
