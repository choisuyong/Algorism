# N개의 원소를 포함하고 있는 오름차순으로 정렬된 수열에서
# X가 등장하는 횟수를 계산하시오

from bisect import bisect_left,bisect_right

n, k = map(int, input().split(' '))
array = list(map(int, input().split()))

left_value = bisect_left(array,k)
righ_value = bisect_right(array,k)

if( righ_value - left_value ) == 0 :
    print(-1)
else :
    print( righ_value - left_value)