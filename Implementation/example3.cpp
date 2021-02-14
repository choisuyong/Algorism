// # 문자열 재정렬
// # 알파벳 대문자와 숫자로만 구성된 문자열을 이하의 기준에 맞추어 재정렬 하시오
// # ----- 기준
// # 1. 알파벳을 오름차순으로 정렬
// # 2. 오름차순으로 정렬된 알파벳 뒤에 숫자를 더한값을 출력

#include <iostream>
#include <time.h>
#include <vector>
#include <string>
#include <time.h>

using namespace std;

int main(void) {

    string str;
    cin >> str;

    clock_t start,end;
    start = clock();
    vector<char> result;
    int number = 0;
    for(int i = 0 ; i < str.length() ; i++ ) {
        if( isalpha(str[i]) ) {
            result.push_back(str[i]);
        }else {
            number += str[i] - '0';
        }
    }

    sort(result.begin(),result.end());

    cout << "결과 문자열 : ";
    for( int i = 0 ; i < result.size() ; i ++ ) {
        cout << result[i] ;
    }

    if( number != 0 ) cout << number << endl;
    end = clock();
    cout << "실행시간 : " << double(end - start) << endl;
}