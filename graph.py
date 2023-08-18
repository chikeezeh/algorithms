from collections import deque
# use adjacent list to represent graph, key = node, value = neighbors
graph = {
    'a':['c','b'],
    'b':['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f':[]
}

# this uses a stack to keep track of nodes
def dfs_graph(graph, start):
    arr = []
    stack = []
    stack.append(start)
    while stack:
        curr = stack.pop()
        arr.append(curr)
        for i in graph[curr]:
            stack.append(i)
    return arr

print(dfs_graph(graph,'a'))

# this uses queues to keep track of nodes.
def bfs_graph(graph, start):
    arr = []
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        arr.append(curr)
        for i in graph[curr]:
            queue.append(i)
    return arr

print(bfs_graph(graph,'a'))

def dfs_graph_rec(graph, start, arr=[]):
    arr.append(start)
    for i in graph[start]:
        dfs_graph_rec(graph,i,arr)
    
    return arr

print(dfs_graph_rec(graph,'a'))
