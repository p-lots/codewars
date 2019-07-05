#include <algorithm>
#include <vector>

int findOdd(const std::vector<int>& numbers)
{
    for (const auto &n : numbers) {
        if (std::count(numbers.begin(), numbers.end(), n) % 2 == 1) return n;
    }
    return 0;
}