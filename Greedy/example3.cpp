// # 한 마을에 모험가가 N명이 있습니다. 각 모험가를 대상으로 공포도를 조사하였습니다.
// # 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있습니다.
// # 최대 몇개의 모험가 그룹을 만들 수 있는지 구하시오

#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>

using namespace std;
vector<int> fear;

int main( void ) {
    int count;
    cin >> count;

    for(int i = 0 ; i < count ; i ++ ) {
        int x;
        cin >> x;
        fear.push_back(x);
    }
    clock_t start,end;
    start = clock();

    sort(fear.begin(),fear.end());

    int result = 0;
    int cnt =0;

    for(int i = 0 ; i < count ; i ++ ) {
        cnt +=1;
        if( cnt >= fear[i] ) {
            result +=1;
            cnt = 0;
        }
    }
    end = clock();
    cout << "총 그룹 수 : " << result << endl;
    cout << "실행시간 : " << end - start << "ms" << endl;
}