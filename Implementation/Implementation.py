# 풀이를 떠올리는것은 쉽지만 소스코드로 옮기기 어려운 문제
# 알고리즘은 간단한데 코드가 길어지는 문제
# 실수 연산을 다루고 특정 소수점까지 출력하는 문제
# 문자열을 끊어처리하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제 등

# 상하 좌우 
# N * N크기의 정사각형 공간위에서 커맨드에 따라 움직임
# 커맨드 L R U D : 왼쪽 오른쪽 위 아래 
import time

n = int(input())
x, y = 1,1
plans = input().split()
move_types = ['U','D','L','R']
dx = [0, 0, -1 , 1]
dy = [1, -1, 0, 0]

start_time = time.time()
for plan in plans :
    for i in range(len(move_types)) :
        if plan == move_types[i] :
                nx = x + dx[i]
                ny = y + dy[i]
    if nx < 1 or ny < 1  or nx > n or ny > n :
         continue
    x,y = nx, ny          
print("x : ", x,"y : ", y)
print("실행시간 : ", time.time() - start_time)