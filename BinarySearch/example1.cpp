#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int count_range(vector<int>&array, int leftValue, int rightValue) {
    vector<int>::iterator rightIndex = upper_bound(array.begin(), array.end(), rightValue);
    vector<int>::iterator leftIndex = lower_bound(array.begin(), array.end(), leftValue);
    return rightIndex - leftIndex;
}

int main() {
    int n, x;
    vector<int> array;

    cin >> n >> x;

    for(int i =0 ; i < n ; i ++ ) {
        int temp;
        cin >> temp;
        array.push_back(temp);
    }

    int result = count_range(array, x, x);

    if(result == 0 ) cout << "-1";
    else cout << result;

}