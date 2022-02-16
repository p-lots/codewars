#include <algorithm>
#include <vector>
using namespace std;

int min(vector<int> list)
{
    sort(list.begin(), list.end());
    return list.front();
}

int max(vector<int> list)
{
    sort(list.begin(), list.end());
    return list.back();
}