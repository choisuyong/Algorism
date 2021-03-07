#include <iostream>
#include <vector>

#define INF 1e9

using namespace std;

int n, m;
int graph[501][501];

int main(void) {

    cin >> n >> m ;

    for(int i = 0 ; i < 501 ; i ++ ) {
        fill(graph[i],graph[i]+501, INF);
    }
    
    for(int a = 0 ; a <= n ; a ++ ) {
        for(int b = 0 ; b <=n ; b ++ ) {
            if(a == b) graph[a][b] = 0;
        }
    }

    for(int i = 0 ; i < m ; i ++ ) {
        int a,b,c;
        cin >> a >> b >> c;
        graph[a][b] = c;
    }

    for(int k = 0 ; k <= n ; k ++ ) {
        for(int a = 0 ; a <= n ; a ++ ) {
            for(int b = 0 ; b <= n ; b ++ ) {
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]);
            }
        }
    }

    for(int a = 0 ; a <= n ; a ++ ) {
        for(int b = 0 ; b<= n ; b ++ ) {
            if(graph[a][b] == INF ) {
                cout << "INF" << " ";
            }else {
                cout << graph[a][b] << " ";
            }
        }
        cout << "" << endl;
    }
}