#include <algorithm>
#include <numeric>

std::string meanVsMedian(std::vector<int> numbers)
{
    double mean = std::accumulate(numbers.begin(), numbers.end(), 0.0) / static_cast<double>(numbers.size());
    std::sort(numbers.begin(), numbers.end());
    int median = numbers.at(numbers.size() / 2);
    return mean > median ? "mean" : mean == median ? "same" : "median";
}