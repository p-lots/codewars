#include <algorithm>
#include <numeric>
#include <vector>

int sumOfDifferences(const std::vector<int>& arr)
{
    if (arr.size() < 2) return 0;
    auto arr_sorted = arr;
    int ret = 0;
    std::sort(arr_sorted.begin(), arr_sorted.end(), std::greater<int>());
    for (unsigned i = 0; i < arr_sorted.size() - 1; i++) {
        ret += arr_sorted[i] - arr_sorted[i + 1];
    }
    return ret;
}