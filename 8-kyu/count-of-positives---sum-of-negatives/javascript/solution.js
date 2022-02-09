#include <algorithm>
#include <cmath>
#include <numeric>
#include <vector>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.empty()) return { };
    int first = int(std::count_if(input.begin(), input.end(),
        [](const int &n) { return n > 0; }));
    int second = 0;
    for (int n : input) {
        if (n < 0) second += std::abs(n);
    }
    return { first, -second };
}