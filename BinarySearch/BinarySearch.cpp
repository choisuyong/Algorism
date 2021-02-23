#include "BinarySearch.h"

int main() {
    int n, target;
    vector<int> a;

    cin >> n >> target;

    for(int i =0 ; i < n ; i ++ ) {
        int x;
        cin >> x;
        a.push_back(x);
    }

    int result = binarySearch(a,target,0,n-1);

    if(result == -1 ) {
        cout << "해당하는 값이 없습니다";
    }else {
        cout << result + 1 ;
    }



}