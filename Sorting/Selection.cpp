#include <iostream>

using namespace std;

int main() {

    int size = 10;  
    int array[10] = {7,5,9,0,3,1,6,2,4,8};

    for(int i = 0 ; i < size ; i ++ ) {
        int min_index = i;
        for(int j = i+1 ; j < size ; j ++ ) {
            if( array[min_index] > array[j] ) {
                int temp = array[min_index];
                array[min_index] = array[j];
                array[j] = temp;
            }
        }
        cout << array[i] << " " ;
    }

}