#include <algorithm>t

int tram(int stops, const vector<int>& a, const vector<int>& b)
{
    int curr_capacity = 0, ret = 0;
    for (unsigned i = 0; i < stops; i++) {
        curr_capacity += b[i] - a[i];
        ret = std::max(curr_capacity, ret);
    }
    return ret;
}