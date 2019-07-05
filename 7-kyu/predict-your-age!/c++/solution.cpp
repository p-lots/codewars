#include <math.h>
#include <numeric>
#include <vector>

int predictAge(int age1, int age2, int age3, int age4, int age5, int age6, int age7, int age8)
{
    std::vector<int> ages = { age1, age2, age3, age4, age5, age6, age7, age8 };
    auto ret = std::accumulate(ages.begin(), ages.end(), 0, 
        [](int result, int accum) {
            return result + accum * accum;
        });
    return sqrt(ret) / 2;
}