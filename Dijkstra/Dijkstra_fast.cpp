#include <iostream>
#include <queue>
#include <vector>

#define INF 1e9

using namespace std;

int n,m,start;
vector<pair<int,int> > graph[10001];

int d[10001];

void dijkstra(int start ) {
    priority_queue<pair<int,int> > pq;
    pq.push(make_pair(0,start));
    d[start] = 0; 

    while(!pq.empty()) {
        
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if(dist < d[now]) continue;

        for(int i =0 ; i < graph[now].size() ; i++ ) {
            int cost = dist + graph[now][i].first;

            if(cost < d[graph[now][i].first] ) {
                d[graph[now][i].first] = cost;
                // 기본적으로 최대힙이기에 -를 붙여서 최소힙으로 움직일 수 있게힘
                pq.push(make_pair(-cost, graph[now][i].first));
            }
        } 
    }

}

int main(void) {
    cin >> n >> m >> start;

    for(int i = 0 ; i < m ; i ++ ) {
        int a,b,c;
        cin >> a >> b >> c;
        graph[a].push_back(make_pair(b,c));
    }

    fill_n(d,10001,INF);
    dijkstra(start);

    for(int i = 0 ; i <= n ; i ++ ) {
        if ( d[i] == INF ) cout << " INF" << endl;
        else cout << d[i] << endl;
    }
}
