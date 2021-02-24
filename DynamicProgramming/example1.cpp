#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    vector<int> array;
    vector<int> d;

    cin >> n ;
    
    for(int i = 0 ; i < n ; i ++) {
        int y;
        cin >> y;
        array.push_back(y);
    }

    d[0] = array[0];
    d[1] = max ( array[0], array[1] );

    for(int i = 2 ; i < n ; i ++ ) {
        d[i] = max(d[i-1], d[i-2] + array[i] );
    }


}