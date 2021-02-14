# 너비우선탐색 : 가까운 노드부터 우선적으로 탐색하는 알고리즘
# 큐 자료구조를 이용하며 구체적인 동작과정은 다음과 같음

# 탐색 시작 노드를 큐에 삽입하고 방문처리
# 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 위의 과정을 더이상 수행하지 못할때까지 반복

# 각 간선의 비용이 동일한 조건에 최단거리를 찾을때 사용
from collections import deque
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

def bfs( graph, start, visited ) :
    Queue = deque([start])
    visited[start] = True

    while Queue :
        v = Queue.popleft()
        print(v, end=' ')

        for i in graph[v] :
            if not visited[i] :
                Queue.append(i)
                visited[i] = True

print(bfs(graph,1,visited))