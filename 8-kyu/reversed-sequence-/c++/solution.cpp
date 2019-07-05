#include <algorithm>
#include <numeric>

std::vector<int> reverseSeq(int n) {
    std::vector<int> ret(n);
    std::iota(ret.begin(), ret.end(), 1);
    std::reverse(ret.begin(), ret.end());
    return ret;
}