#include <numeric>
#include <vector>

std::vector<int> arrayLeaders(const std::vector<int>& numbers)
{
    std::vector<int> sums;
    for (auto it = numbers.begin(); it != numbers.end(); it++) {
        sums.push_back(std::accumulate(it, numbers.end(), 0) - *it);
    }
    std::vector<int> ret;
    for (unsigned i = 0; i < numbers.size(); i++) {
        if (numbers[i] > sums[i]) ret.push_back(numbers[i]);
    }
    return ret;
}