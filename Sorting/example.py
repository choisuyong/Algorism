# 두 배열 A B를 최대 K번 교체 가능합니다.
# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최대값을 구하시오

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k) :
    if a[i] < b [i] :
        a[i],b[i] = b[i],a[i]
    else :
        break        

print(sum(a))
