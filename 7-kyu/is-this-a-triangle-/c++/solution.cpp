#include <vector>
#include <algorithm>

namespace Triangle
{
    bool isTriangle(long long a, long long b, long long c)
    {
        if (a <= 0 || b <= 0 || c <= 0) return false;
        std::vector<long long> vec = { a, b, c };
        std::sort(vec.begin(), vec.end());
        long long smallest = vec.at(0);
        long long middle = vec.at(1);
        long long largest = vec.at(2);
        if (smallest + middle <= largest) return false;
        return true;
    }
};