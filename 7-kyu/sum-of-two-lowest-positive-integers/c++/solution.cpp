#include <algorithm>

long sumTwoSmallestNumbers(std::vector<int> numbers)
{
    long min = *(std::min_element(numbers.begin(), numbers.end()));
    long next_min = *(std::max_element(numbers.begin(), numbers.end()));
    for (const int n : numbers) {
        if (n < next_min && n > min) next_min = n;
    }
    return min + next_min;
}