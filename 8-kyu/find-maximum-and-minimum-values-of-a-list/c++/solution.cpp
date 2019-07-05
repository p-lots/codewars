#include <vector>
using namespace std;

int min(vector<int> list){
    
    auto min = list[0];
    for (int n : list) {
        if (n < min) min = n;
    }
    return min;
}

int max(vector<int> list){
    
    auto max = list[0];
    for (int n : list) {
        if (n > max) max = n;
    }
    return max;
}