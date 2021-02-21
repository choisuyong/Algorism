# 처리되지 않은 데이터를 하나씩 골라 삽입하는 알고리즘
# 해당 원소와 삽입 위치의 크기를 비교하여 크기가 작으면 왼쪽, 크면 오른쪽으로 입력
# 배열의 마지막 부터 확인
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)) :
    for j in range(i, 0, -1) :
        if( array[j] < array[j-1]) :
            array[j],array[j-1] = array[j-1],array[j]
        else :
            break
print(array)       