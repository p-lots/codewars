#include <algorithm>
#include <cmath>
#include <numeric>
#include <vector>

using namespace std; 

unsigned long long minValue (vector<int> values)
{
    std::sort(values.begin(), values.end());
    values.erase(std::unique(values.begin(), values.end()), values.end());
    int power = 0;
    unsigned long long result = 0;
    for (auto it = values.rbegin(); it != values.rend(); it++) {
        result += std::pow(10, power++) * (*it);
    }
    return result;
}