import time

#  각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S에 대하여 왼쪽부터 오른쪽으로 하나씩
#  모든 숫자를 확인하여 * 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하여라

data = input()

start_time = time.time()
result = int(data[0])

for i in range(1,len(data)) :
    num = int(data[i])

    if(num > 1 ) :
        result += num
    else :
        result *= num

print(result)
print("실행시간 : ", time.time() - start_time)