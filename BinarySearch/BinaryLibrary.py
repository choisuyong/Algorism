# bisec_left( array, target) 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
# bisec_right( array, target) 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환


from bisect import bisect_left,bisect_right

# a = [1,2,4,4,8]
# x = 4

# print(bisect_left(a,x))
# print(bisect_right(a,x))

#값이 특정 범위에 속하는 데이터 개수 구하기

def count_by_range(a, left_value,right_value ) :
    left_value = bisect_left(a, left_value)
    right_value = bisect_right(a, right_value)

    return right_value - left_value    

a = [1,2,3,3,3,3,4,4,8,9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

#값이 -1에서 3 밤위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))