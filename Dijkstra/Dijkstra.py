# 그리디 알고리즘에 속함 : 매 상황마다 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정 반복
# 단계를 거치며 처리된 노드의 최단거리는 고정되어 바뀌지 않음

import sys
input = sys.readline()
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [{} for i in range(n+1)]
visited = [False] * (n+1)
distance = [1e9] * (n+1)

for _ in range(n) :
    a,b,c = map(input().split())
    # a 노드에서 b노드까지의 거리가 c
    graph[a].append(b,c)

def get_smallest_node() :
    min_value = INF
    index = 0
    for i in range(1,n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i] 
            index = i
    return index

def djkstra() :
    distance[start] = 0
    visited[start] = True

    for j in graph[start] : 
        distance[j[0]] = j[1]

    for i in range(1, n-1) :            
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now] :
            cost = distance[now] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost
 
djkstra(start)

for i in range(n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])        
