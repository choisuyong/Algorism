# 우선순위 큐를 이용하여 구현
# 자료구조로 Heap을 사용 : LogN만큼의 시간복잡도
# 최소힙 / 최대힙  자료를 꺼내는 순서에 따른 구분

"""
import heapq

def heapsort(itertable) :
    h = []
    result  = []
    for value in itertable :
        heapq.heappush(h,value)
        #heapq.heappush(h,-value)
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
        #result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] *(n+1) 

for _ in range(m) :
    a,b,c = map(int, input().spilit())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for i in graph[now] :
            cost = dist+ i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(cost,i[0])

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])                
