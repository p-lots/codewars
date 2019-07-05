#include <cmath>

long long reverseNumber(long long n)
{
    if (n > -10 && n < 10) return n;
    bool less_than_zero = n < 0;
    n = std::llabs(n);
    long long ret = 0;
    long long mult = std::floor(std::log10(n));
    while (n > 0) {
        ret += (n % 10) * std::pow(10, mult);
        mult--;
        n /= 10;
    }
    return ret * (less_than_zero ? -1 : 1);
}