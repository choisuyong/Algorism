# 8*8의 체스판에서 나이트의 위치가 주어졌을때 나이트가 이동할 수 있는 경우의 수를 출력하시오
import time
input_data = input()
row = int(input_data[1])
collom = int(ord(input_data[0])) - int(ord('a')) +1

steps = [(-2,-1), (-1,-2), (1,-2),(2,-1), (2,1),(1,2),(-1,-2),(-2,-1)]

result = 0
start = time.time()
for step in steps :
    next_row = row + step[0]
    next_collom = row + step[1]
    
    if( next_row < 1 or next_collom < 1 or next_row > 8 or next_collom > 8) :
        continue

    result +=1
end = time.time()
print("이동 가능한 경우의 수 :", result)
print("실행 시간  : ", end - start)    
