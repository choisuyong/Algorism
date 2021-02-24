# 식량 창고를 약탈 하기 위헤서 다음과 같은 규칙을 따름
# 인접한 창고를 공격할 경우 들키기에 최소한 한칸 이상 떨어진 식량 창고를 공격해야함
# 식량 창고에 대한 정보가 주어졌을때 얻을 수 있는 식량의 최대값을 구하여라

n = map(int, input())
array = list(map(int, input().split()))
result = 0

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n) :
    d[i] =  max(d[i-1], d[i-2] + array[i])

print(d[n-1])
