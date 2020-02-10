#include <algorithm>

std::vector<int> maps(const std::vector<int> & values) {
    std::vector<int> ret = values;
    std::transform(ret.begin(), ret.end(), ret.begin(), [](int n) { return n + n; });
    return ret;
}