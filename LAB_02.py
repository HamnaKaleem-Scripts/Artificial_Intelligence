def dfs(graph,node,path=None):
    if path is None:
        path=[]
    print(node,end=" ")
    if node not in path:
        path.append(node)
    for i in graph[node]:
        if i not in path:
            dfs(graph,i,path)
            
graph = {
    'A': ['D', 'E'],
    'B': ['A'],
    'C': ['B', 'D'],
    'D': [],
    'E': ['C'],
    'F': ['E']


}
dfs(graph, 'A')


print()

def bfs(graph ,node):
    path=[]
    queue=[node]
    while queue:
        node=queue.pop(0)
        if node not in path:
            path.append(node)
            # print(a,end=" ")
            for i in graph [node]:
                if i not in path and i not in queue:
                    queue.append (i)
    print (path)

graph = {
    'A': ['D', 'E'],
    'B': ['A'],
    'C': ['B', 'D'],
    'D': [],
    'E': ['C'],
    'F': ['E']
}

bfs(graph, 'A')
 
                  