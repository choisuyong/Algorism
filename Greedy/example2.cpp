// #  각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S에 대하여 왼쪽부터 오른쪽으로 하나씩
// #  모든 숫자를 확인하여 * 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하여라

#include <iostream>
#include <time.h>
using namespace std;

string str;

int main( void ) {
    cin >> str;
    clock_t start, end;
    start = clock();

    long long result = str[0]-'0';

    for(int i = 0 ;i < str.size() ; i++ ) {
        int num = str[i]  - '0';
        if( num <= 1 || result <= 1 ) result += num;
        else result *= num;
    }
    cout << "결과 값 : " << result << endl;
    end = clock();
    cout << "실행시간 : " << double(end - start) <<"ms" <<endl;
}