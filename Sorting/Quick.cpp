#include <iostream>
#include <algorithm>

using namespace std;

void quick_sort(int* array,int start, int end ) {
    if(start >= end ) return;
    int pivot = start;
    int left = start +1;
    int right = end;

    while( left <= right) {
        while( left <= end && array[left] <= array[pivot] ) left++;
        while( right > start && array[right] >= array[pivot] ) right--;
        if( left > right ) swap( array[pivot],array[right]);
        else swap(array[left],array[right]);
    }

    quick_sort(array,start,right-1);
    quick_sort(array,right+1,end);
}

int main() {
    int size = 10;
    int array[10] = {7,5,9,0,3,1,6,2,4,8};

    quick_sort(array,0,size-1);

    for(int i =0 ; i < size ; i ++ ) {
        cout << array[i] << " ";
    }

}