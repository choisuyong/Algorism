#include "example2.h"

int main() {
    cin >> n >> m;

    for(int i = 0 ; i < n ; i ++ ) {
        for(int j = 0 ; j < m ; j ++ ) {
            scanf("%1d",&graph[i][j]);
        }
    }
    cout << bfs(0,0) << endl;
}