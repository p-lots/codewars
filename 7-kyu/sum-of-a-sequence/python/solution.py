#include <numeric>
#include <vector>

int sequenceSum(int start, int end, int step)
{
    if (start > end) return 0;
    std::vector<int> v;
    for (unsigned i = start; i <= end; i += step) {
        v.push_back(i);
    }
    return std::accumulate(v.begin(), v.end(), 0);
}