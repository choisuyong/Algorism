# 정렬되어있는 리스트에서 탐색 범위를 절반씩 조렵가며 데이터를 탐색
# 시작점, 끝점, 중간점을 이용하여 탐색 범위를 지정
# 시간복잡도는 LogN

def binary_search(array,target,start,end) :
    if start > end :
        return None
    mid = (start + end ) // 2

    if target == array[mid] :
        return mid
    elif array[mid] > target :
        return binary_search(array,target,start,mid-1)
    else :
        return binary_search(array,target,mid+1,end)

n,target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array,target,0,n-1)

if result == None :
    print("값이 존재하지 않습니다")
else :
    print(result +1 )    