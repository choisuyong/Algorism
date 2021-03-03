# 특정한 값의 전투력을 보유한 N명의 병사가 무작위로 나열되어있습니다.
# 병사를 배치할 때는 전투력이 높은 병사가 앞족에 오도록 내림차순으로 배치
# 배치 과정에서는 특정한 위치에 있는 병사를 열외시킵니다. 
# 남아있는 병사의 수가 최대가 되도록 하고싶습니다.
# 가장 긴 증가하는 부분수열(LIS)로 알려진 전형적인 다이나믹 프로그래밍

n = int(input())
array = list(map(int, input().split()))

array.reverse()
dp = [1] * n

for i in range(1,n) :
    for j in range(0,1) :
        if array[i] < array[j] :
            dp[i] = max(dp[i], dp[j]+1)
            
print(n - max(dp) )

