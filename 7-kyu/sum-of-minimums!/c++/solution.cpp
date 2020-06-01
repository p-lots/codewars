#include <algorithm>
#include <vector>

int sum_of_minimums(const std::vector<std::vector<int>> &numbers)
{
    int ret = 0;
    for (const auto &row : numbers) {
        auto lowest = *std::min_element(row.begin(), row.end());
        ret += lowest;
    }
    return ret;
}