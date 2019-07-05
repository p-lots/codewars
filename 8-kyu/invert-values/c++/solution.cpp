#include <algorithm>
#include <vector>

std::vector<int> invert(std::vector<int> values)
{
    if (values.empty()) return std::vector<int>();
    std::transform(values.begin(), values.end(), values.begin(), [](int &n) { return -n; });
    return values;
}