import time
#  어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 수행하려고 함. 
#  단 두번째 연산은 N이 K로 나누어 떨어질때만 선택 가능
#  1. N에서 1을 뺍니다.
#  2. N을 K로 나눕니다.

n, k = map(int, input().split())
start_time = time.time()
result = 0

while True :
    target = ( n//k ) *k
    result += ( n -  target)

    n = target
    if( n < k ) :
        break
    result += 1
    n //= k

result += (n-1)
print(result)
print(time.time() - start_time)

        