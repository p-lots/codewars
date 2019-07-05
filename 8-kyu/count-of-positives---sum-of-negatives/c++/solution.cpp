#include <algorithm>
#include <numeric>
#include <vector>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.empty()) return { };
    input.erase(std::remove(input.begin(), input.end(), 0), input.end());
    auto it = std::remove_if(input.begin(), input.end(), [](const int &n) { return n < 0; });
    int first = static_cast<int>(std::distance(input.begin(), it));
    int second = std::accumulate(it, input.end(), 0);
    return { first, second };
}