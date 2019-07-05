#include <algorithm>

long sumTwoSmallestNumbers(std::vector<int> numbers)
{
    std::sort(numbers.begin(), numbers.end());
    return static_cast<long>(numbers.at(0)) + static_cast<long>(numbers.at(1));
}