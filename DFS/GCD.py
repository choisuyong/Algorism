# 최대공약수를 구하는 유클리드 호제법을 구현

def GCD( a, b ) :
    if a % b == 0 :
        return b
    else :
        return GCD( b, a % b )

print("최대공약수 : ", GCD( 192, 162))    