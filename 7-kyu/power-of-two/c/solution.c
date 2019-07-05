#include <stdbool.h>

bool power_of_two(const int x)
{
    if (x == 1) return true;
    else if (x % 2 == 1) return false;
    unsigned long long n = 1;
    while (n <= x) {
        n <<= 1;
        if (n == x) return true;
    }
    return false;
}