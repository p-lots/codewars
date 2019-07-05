#include <algorithm>
#include <cmath>
#include <numeric>
#include <vector>

int square_sum(const std::vector<int>& numbers)
{
    return std::accumulate(numbers.begin(), numbers.end(), 0, 
        [](const int &lhs, const int &rhs) {
            return lhs + std::pow(rhs, 2);
        });
}