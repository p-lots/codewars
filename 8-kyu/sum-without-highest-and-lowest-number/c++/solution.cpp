#include <algorithm>
#include <numeric>
#include <vector>

int sum(std::vector<int> numbers)
{
    if (numbers.empty() || numbers.size() == 1) return 0;
    std::sort(numbers.begin(), numbers.end());
    return std::accumulate(numbers.begin() + 1, numbers.end() - 1, 0);
}