#최적의 해를 얻기 위한 알고리즘. 
#항상 최적의 해라고 할 수는 없음. 현재 상황에서 가장 최적의 해를 구해내는 알고리즘

n = 1260
count = 0

array = [500,100,50,10]

for coin in array :
    print(coin)
    count += n // coin
    n %= coin

print(count)