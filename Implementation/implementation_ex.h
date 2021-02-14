#include <iostream>
#include <vector>
#include <string>
#include <time.h>

using namespace std;

int n;
string plans;
int x, y;

int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
char move_types[4] = {'R','L','U','D'};