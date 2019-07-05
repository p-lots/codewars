#include <cmath>

int divisors(long long n)
{
    if (n <= 0) return 0;
    else if (n == 1) return 1;
    int count = 2;
    for (long long i = 2; i <= std::sqrt(n); i++) {
        if (n % i == 0 && i != std::sqrt(n)) count += 2;
        else if (n % i == 0) count++;
    }
    return count;
}