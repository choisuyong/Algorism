# n*m 크기의 금광이 있고, 칸으로 나누어짐
# 각 칸에는 특정 크기에 금이 들어있음.
# 첫번째의 어느 열의 행에서든 출발 가능하며 오른쪽 위, 오른쪽, 오른족 아래의 위치로만 이동 가능
# 채굴자가 얻는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

for tc in range(int(input())) :
    n,m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0

    for i in range(n) :
        dp.append(array[index:index + m] )
        index += m

    for j in range(1,m) :
        for i in range(n) :
            if i == 0 : left_up = 0
            else : left_up = dp[i-1][j-1]

            if i == n-1 : left_down = 0
            else : left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)

    result = 0
    for i in range(n) :
        result = max(result, dp[i][m-1])
    print(result)                 




