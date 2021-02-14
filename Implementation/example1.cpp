// # 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는
// # 모든 경우의 수를 구하는 프로그램을 작성하시오

#include <iostream>
using namespace std;
int h,cnt;

bool check(int h, int m, int s ) {
    if( ( h % 10 == 3) || (m / 10 == 3) || (m % 10 ==3) || (s/ 10 ==3) || (s %10 == 3) )
        return true;
    return false;
}

int main( void ) {
    
    cin >> h;
    for(int i =0 ; i <=h ; i ++ ) {
        for(int m = 0 ;m < 60 ; m ++ ) {
            for(int s = 0 ; s < 60 ; s++ ) {
                if(check(h,m,s)) cnt++;
            }
        }
    }
    cout << "총 실행 경우의 수 : " << cnt << endl;
}
