#include <algorithm>
#include <numeric>

int house_numbers_sum(const std::vector<int> &arr)
{
    auto it = std::find(arr.begin(), arr.end(), 0);
    return std::accumulate(arr.begin(), it, 0);
}