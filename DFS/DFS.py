# 깊이를 우선으로 하여 탐색하는 알고리즘
# 스택을 이용함

# 탐색 시작노드를 스택에 삽입하고 방문처리
# 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에넣고 방문처리
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# 더이상 노드를 꺼낼 수 없을때까지 동작을 반복해서 수행

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def dfs (graph, v, visited ) :
    visited[v] = True
    print(v, end=' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph,i,visited)

dfs(graph,1,visited)

for i in graph[i] :
    print("i : ", i)
    print("graph[i] " , graph[i])