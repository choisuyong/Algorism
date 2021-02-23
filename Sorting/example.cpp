#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(int x, int y ) {
    return x > y;
}
int main() {
    int n,k;
    cin >> n >> k ;

    vector<int> a,b;
    for(int i =0; i < n ; i ++ ) {
        int x;
        cin >> x;
        a.push_back(x);
    }
    for(int i =0; i < n ; i ++ ) {
        int y;
        cin >>y;
        b.push_back(y);
    }

    sort(a.begin(),a.end());
    sort(b.begin(),b.end(),compare);
    
    for(int i = 0 ; i < k ; i++ ) {
        if(a[i] < b[i]) swap(a[i],b[i]) ;
        else break;
    }

    int result =0;
    for(int i =0 ; i < n ; i ++ ) {
        result += a[i];
    }    
    cout << result;

}