// # 상하 좌우 
// # N * N크기의 정사각형 공간위에서 커맨드에 따라 움직임
// # 커맨드 L R U D : 왼쪽 오른쪽 위 아래 

#include "implementation_ex.h"

int main( void ) {
    
    cin >> n;
    cin.ignore();

    getline( cin, plans);

    clock_t start,end;
    start = clock();

    for( int i = 0 ; i < plans.size() ; i ++ ) {
        char plan = plans[i];
        int nx = -1, ny = -1;

        for(int j = 0; j < 4 ; j ++ ) {
            if( plan == move_types[j]) {
                nx = x + dx[j];
                ny = y + dy[j];
            }
        }

        if( nx < 0 || ny < 0 || nx > n || ny > n ) continue;
        
        x = nx;
        y = ny;
    }
    
    end = clock();
    cout << "x : " << x << " y : " << y << endl;
    cout << "실행시간 : " << double(end- start) << "ms" << endl;
}
