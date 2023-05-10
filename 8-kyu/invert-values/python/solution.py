#include <algorithm>
#include <vector>

std::vector<int> invert(std::vector<int> values)
{
    std::transform(values.begin(), values.end(), values.begin(), 
        [](int &n) { return -n; });
    return values;
}