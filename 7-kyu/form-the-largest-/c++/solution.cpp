#include <algorithm>
#include <functional>
#include <vector>

long long int maxNumber(long long int  number) 
{
    std::vector<int> digits;
    while (number > 0) {
        digits.push_back(number % 10);
        number /= 10;
    }
    std::sort(digits.begin(), digits.end(), std::greater<>());
    long long int power = 1;
    long long int ret = 0;
    for (auto r_it = digits.crbegin(); r_it != digits.crend(); r_it++) {
        ret += *r_it * power;
        power *= 10;
    }
    return ret;
}