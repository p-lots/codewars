#include <cmath>
#include <vector>

std::vector<bool> makeSieve()
{
    std::vector<bool> ret(2000000, true);
    ret[0] = false;
    ret[1] = false;
    for (unsigned i = 2; i < std::sqrt(2000000); i++) {
        if (ret[i]) {
            for (unsigned j = i * i; j < 2000000; j += i) {
                ret[j] = false;
            }
        }
    }
    return ret;
}

unsigned long long numPrimorial (unsigned short int number)
{
    auto primes = makeSieve();
    unsigned i = 0, primesCount = 0;
    unsigned long long ret = 1;
    while (i < primes.size() && primesCount < number) {
        if (primes[i]) {
            ret *= i;
            primesCount++;
        }
        i++;
    }
    return ret;
}