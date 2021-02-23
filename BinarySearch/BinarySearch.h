#include <iostream>
#include <vector>

using namespace std;

int binarySearch(vector<int>& array, int target,int start, int end) {
    while( start <= end ) {
        int mid = (start + end ) / 2;
        if(array[mid] == target ) return mid;
        else if (array[mid] > target ) end = mid-1;
        else start = mid+1;
    }
    return -1;
}