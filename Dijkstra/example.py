# 첫째줄에 도시의 개수 N, 통로의 개수 M, 메세지를 보내고자하는 도시 C가 주어짐
# 둘째줄 부터 M+1번째줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다.
#    X 에서 Y도시까지 이어지는 통로의 시간이 Z
# 도시C에서 보낸 메세지를 받는 도시의 총개수와 걸리는 시간을 공백으로 구분하여 출력하라 
import heapq
import sys
input = sys.stdin.readline

n,m,start = map(int, input().split())
INF = 1e9
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m) :
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist,now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
cnt = 0
max_distance = 0
for d in distance :
    if d != INF :
        cnt += 1
        max_distance = max(max_distance, d)
print(cnt-1, max_distance)

    

