# n*m 크기의 직사각형 형태의 미로
# 시작과 마지막은 항상 1, 
# 0은 통과 할 수 없음, 1은 통과가능
# 최단거리를 확인

from collections import deque

def bfs( x, y ) :
    queue = deque()
    queue.append( (x,y) )

    while queue :
        x,y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] +1
                queue.append( (nx,ny))

    return graph[n-1][m-1]        
n,m = map(int,input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(bfs(0,0))
