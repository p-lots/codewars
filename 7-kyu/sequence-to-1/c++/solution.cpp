#include <algorithm>
#include <numeric>

std::vector<int> seqToOne(int n) {
    std::vector<int> ret;
    if (n > 0) {
        ret = std::vector<int>(n);
        std::iota(ret.begin(), ret.end(), 1);
        std::reverse(ret.begin(), ret.end());
    }
    else {
        int dist = 1 - n + 1;
        ret = std::vector<int>(dist);
        std::iota(ret.begin(), ret.end(), n);
    }   
    return ret;
}