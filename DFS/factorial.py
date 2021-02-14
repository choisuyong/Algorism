# DFS/BFS 대표적인 그래프 탐색 알고리즘
# 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

# 자료구조
# stack - 선입후출(먼저 들어온 자료가 나중에 나가는 형식)
# queue - 선입선출(먼저 들어온 자료가 먼저 나가는 형식)

# 재귀함수
# 자기 자신을 다시 호출하는 함수

def factorial( number ) :
    result = 1
    
    for n in range(1,number+1) :
        result *=n
    return result    

def factorial_recursive( n ) :
    if n <= 1 :
        return 1
    return n * factorial_recursive( n -1 )       

print("반복문 팩토리얼 : ", factorial(5))
print("재귀함수 팩토리얼 : ", factorial_recursive(5))