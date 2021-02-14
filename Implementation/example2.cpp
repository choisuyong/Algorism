#include <iostream>
#include <string>
#include <vector>
#include <time.h>

using namespace std;

int main( void ) {

    int dx[8] = {-2,-1,1,2,2,1,-1,-2};
    int dy[8] = {-1,-2,-2,-1,1,2,2,1};
    int result = 0 ;
    clock_t start,end;

    string position;
    cin >> position;

    start = clock();
    int row = position[1] - '0';
    int collom = position[0] - 'a' +1;

    for(int i = 0 ; i < 8 ;i ++) {
        int next_row = row + dx[i];
        int next_collom = collom + dy[i];

        if( next_row < 1 || next_collom < 1 || next_row > 8 || next_collom > 8 ) continue;
        result++;
    }
    end = clock();

    cout << "이동 가능한 경우의 수 : " << result << endl;
    cout << "실행시간 : " << double(end - start) << "ms"<< endl;
}