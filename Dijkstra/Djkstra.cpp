#include <iostream>
#include <vector>

using namespace std;

#define INF 1e9

int n,m,start;
vector<pair<int, int> > graph[10001];
bool visited[10001];
int d[10001];

int getSmallestValue() {
    int min_value = INF;
    int index = 0;

    for(int i =0 ;i < n ; i ++  ) {
        if(d[i] < min_value && !visited[i]) {
            min_value = d[i];
            index = i;
        }
    }
    return index;
}

void dijkstra(int start) {
    d[start] = 0;
    visited[start] = true;

    for(int i = 0 ; i < graph[start].size() ; i ++ ) {
        d[graph[start][i].first] = graph[start][i].second;
    }

    for(int i = 0 ; i < n ; i ++ ) {
        int now = getSmallestValue();
        visited[now] = true;

        for(int j = 0 ; j < graph[now].size() ; j ++ ) {
            int cost = d[now] + graph[now][j].second;
            if(cost < d[graph[now][j].first] ) {
                d[graph[now][j].first] = cost;
            }
        }
    }
}

int main(void) {
    cin >> n >> m >> start;

    for (int i = 0 ; i <= m ; i ++ ) {
        int a,b,c;
        cin >> a >> b >> c;
        graph[a].push_back(make_pair(b,c));
    }

    fill_n(d,10001,INF);

    dijkstra(start);

    for (int i = 0 ; i <= n ; i ++ ) {
        if(d[i] == INF) {
            cout << " INF" << endl;
        }else {
            cout << d[i] << endl;
        }
    }
}
