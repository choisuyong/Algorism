#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int size = 10;  
    int array[10] = {7,5,9,0,3,1,6,2,4,8};

    for(int i = 1 ; i< size ; i ++ ) {
        for(int j = i-1 ; j > 0 ; j-- ) {
            if( array[j-1] > array[j]) {
                swap(array[j],array[j-1]);
            }else {
                break;
            }
        }
    }

    for(int i = 0 ; i < size ; i ++ ) {
        cout << array[i] << " ";
    }

}