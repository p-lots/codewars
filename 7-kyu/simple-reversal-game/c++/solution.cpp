#include <algorithm>
#include <numeric>
#include <vector>

int solve(int n, int k)
{
    if (k >= n) return -2;
    std::vector<int> numbers(n);
    std::iota(numbers.begin(), numbers.end(), 0);
    for (auto it = numbers.begin(); it != numbers.end() - 1; it++) {
        std::reverse(it, numbers.end());
    }
    auto k_pos = std::find(numbers.begin(), numbers.end(), k);
    return std::distance(numbers.begin(), k_pos);
}