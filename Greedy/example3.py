import time
# 한 마을에 모험가가 N명이 있습니다. 각 모험가를 대상으로 공포도를 조사하였습니다.
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있습니다.
# 최대 몇개의 모험가 그룹을 만들 수 있는지 구하시오

number = input()
fear = list(map(int, input().split()))
start_time = time.time()
fear.sort()

result = 0
count = 0

for i in fear :
    count +=1
    if count >= i :
        result += 1
        count = 0

print("총 그룹 수 : ", result)
print("실행시간 : ", time.time() - start_time )