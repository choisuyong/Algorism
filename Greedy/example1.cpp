// #  어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 수행하려고 함. 
// #  단 두번째 연산은 N이 K로 나누어 떨어질때만 선택 가능
// #  1. N에서 1을 뺍니다.
// #  2. N을 K로 나눕니다.
#include <iostream>
#include <time.h>
using namespace std;

int n, k;
int result;

int main( void ) {
    cin >> n >> k;
    clock_t start,end;

    start = clock();
    while( true ) {
        int target = ( n / k ) * k;
        result += (n - target);
        n = target;

        if( n < k ) break;
            result++;
            n /= k; 
    }

    result +=( n-1);
    cout << "결과 값 : " << result << endl;
    end = clock();
    cout << "실행시간 " << double(end - start) << "ms" << endl;
}