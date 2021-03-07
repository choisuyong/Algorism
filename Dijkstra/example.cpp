#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define INF 1e9

int n,m,start;
vector<pair<int,int> > graph[30001];
int d[30001];

void dijkstra(int start ) {

    priority_queue<pair<int, int> >hq;
    hq.push(make_pair(0,start));
    d[start] = 0;

    while(!hq.empty()) {
        int dist = -hq.top().first;
        int now = hq.top().second;
        cout <<dist << " " << now << endl;
        hq.pop();

        if( d[now] < dist) continue;

        for(int i = 0 ; i < graph[now].size() ; i ++ ) {
            int cost = dist + graph[now][i].second;

            if( cost < d[graph[now][i].first] ) {
                d[graph[now][i].first] = cost;
                hq.push(make_pair(-cost, graph[now][i].first));
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

    fill(d,d+30001,INF);

    dijkstra(start);

    int cnt = 0;
    int max_distance = 0;

    for(int i = 0 ; i <=n ; i ++ ) {
        if(d[i] != INF ) {
            cnt +=1;
            max_distance = max(max_distance,d[i]);
        }
    }
    cout << cnt -1 << " " << max_distance << endl;
}

