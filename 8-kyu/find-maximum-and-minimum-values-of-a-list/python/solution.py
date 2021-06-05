#include <vector>
using namespace std;

int min(vector<int> list)
{    
    return *std::min_element(list.begin(), list.end());
}

int max(vector<int> list)
{    
    return *std::max_element(list.begin(), list.end());
}