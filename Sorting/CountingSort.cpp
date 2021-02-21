#include <iostream>
#include <algorithm>

#define MAX_VALUE 9

using namespace std;

int main() {

    int size = 15; 
    int array[15] = {7,5,9,0,3,1,6,2,9,1,4,8,0,5,2};
    int result[MAX_VALUE+1];

    for(int i = 0 ; i < size ; i++ ) {
        result[array[i]] ++;
    }

    for(int i = 0 ; i < MAX_VALUE +1 ; i ++ ) {
        for(int j = 0 ; j < result[i] ; j ++ ) {
            cout << i << ' '; 
        }
    }

}