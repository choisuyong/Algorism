# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는
# 모든 경우의 수를 구하는 프로그램을 작성하시오
import time

n = int(input())

start = time.time()

result = 0
for p in range(n+1) :
    for m in range(60) :
        for s in range(60) :
            if '3' in str(p) + str(m) + str(s) :
                result +=1
end = time.time()
print("모든 경우의 수 : ", result)
print("실행시간 :", end - start)
