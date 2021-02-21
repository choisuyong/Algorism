# 특정 조건이 부합할때만 사용 가능한 알고리즘
# 데이터의 크기 범위가 제한되며 정수형태로 표현할 수 있을때 사용가능
# 데이터가 등장한 갯수만큼 카운트 하여 

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
result = [0] * (max(array)+1)

for i in range(len(array)) :
    result[array[i]] +=1

for i  in range(len(result)) :
    for j in range(result[i]) :
        print(i,end=' ')

