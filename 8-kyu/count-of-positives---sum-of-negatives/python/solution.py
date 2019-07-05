#include <algorithm>
#include <numeric>
#include <vector>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.empty()) return { };
    return {
        int(std::count_if(input.begin(), input.end(),
            [](const int &n) { return n > 0; })),
        std::accumulate(input.begin(), input.end(), 0,
            [](const int &lhs, const int &rhs) {
                if (lhs < 0 && rhs < 0) return lhs + rhs;
                else if (lhs < 0 && !(rhs < 0)) return lhs;
                else if (rhs < 0) return rhs;
                else return 0;
            }
        )};
}