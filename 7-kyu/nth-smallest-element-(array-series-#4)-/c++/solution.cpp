#include <algorithm>
#include <vector>

int nthSmallest (std::vector<int> passed, int nSmallest)
{
    std::sort(passed.begin(), passed.end());
    return passed[nSmallest - 1];
}