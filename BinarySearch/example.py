# 떡 만들기 문제
# 절단기에 높이를 지정하면 줄지어진 떡을 한번에 절단
# 높이가 H보가 긴 떡은 H위의 떡이 잘리고 짧은 떡은 잘리지 않음
# 손님은 잘린 떡의 길이만큼 가져감. 손님이 요청한 길이가 M일때 적어도 M만큼의 떡을 얻기위헤 절단기에
# 설정할 수 있는 높이의 최댓값을 구하시오

n, m = map(int, input().split(' '))
array = list(map(int, input().split()))

result = 0 
start = 0
end = max(array)

while( start <= end ) :
    total = 0
    mid = (start + end) //2

    for x in array :
        if x > mid :
            total += x - mid
    if total < m  :
        end = mid -1
    else :
        result = mid
        start = mid +1

print(result)