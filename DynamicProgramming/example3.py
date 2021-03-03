# N가지 종류의 화폐가 있음. 
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이되도록
# M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성
n,m = map(int, input().split())
array = []

for i in range(n) :
    array.append(int(input()))

d = [10001]*(m+1)
d[0] = 0

for i in range(n) :
    for j in range(array[i],m+1) :
        if d[j-array[i]] != 10001 :
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])

