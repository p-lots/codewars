#include <algorithm>
#include <vector>

std::vector<int> firstNSmallest(const std::vector<int> arr, int n)
{
    std::vector<int> ret;
    if (n == 0 || n > arr.size()) return ret;
    ret = arr;
    if (n == arr.size()) return ret;
    auto arr_sorted = arr;
    std::sort(arr_sorted.begin(), arr_sorted.end());
    for (int i = arr_sorted.size() - 1; i >= n; i--) {
        for (int j = ret.size() - 1; j >= 0; j--) {
            if (arr_sorted[i] == ret[j]) {
                ret.erase(ret.begin() + j);
                break;
            }
        }
    }
    return ret;
}