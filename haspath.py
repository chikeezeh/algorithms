# Given an adjacency list representing a graph, determine if there is a 
# path between to given nodes.
from collections import deque

def haspath(graph, start, end):
    """ This uses DFS to see if there is a path between two given nodes"""
    if start == end:
        return True
    for neighbor in graph[start]:
        if haspath(graph, neighbor, end):
            return True
    
    return False

graph = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}

def haspathb(graph, start, end):
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        if end == curr:
            return True
        for neighbor in graph[curr]:
            queue.append(neighbor)
    return False



print(haspath(graph,'f','j'))
print(haspathb(graph,'f','j'))