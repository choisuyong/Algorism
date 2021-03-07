# 모든 노드에서 다른 모든 노드까지의 최단경로를 모두 계산
# 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행 
# 다만 매 단계마다가 방문하지 않은 노드중에서 최단거리를 찾는 과정이 필요하지 않음
# 2차원 테이블에 최단거리 정보를 저장 / 다이나믹 프로그래밍 유형

INF = 1e9

n = int(input())
m = int(input())

graph = [[INF] *(n+1) for _ in range(n+1)]

for a in range(1,n+1) :
    for b in range(1, n+1 ) :
        if a == b :
            graph[a][b] = 0

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1,n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n +1) :
    for b in range(1,n+1) :
        if graph[a][b] == INF :
            print("INF")
        else :
            print(graph[a][b],end=' ')
    print()

