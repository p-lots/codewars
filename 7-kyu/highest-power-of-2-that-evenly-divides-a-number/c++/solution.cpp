#include <cmath>

unsigned long long solution ( unsigned long long n )
{
    int power = std::log2(n);
    unsigned long long ret = std::pow(2, power);
    while (n % ret != 0) {
        ret = std::pow(2, --power);
    }
    return ret;
}