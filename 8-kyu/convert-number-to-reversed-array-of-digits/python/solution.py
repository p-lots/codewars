#include <cmath>

std::vector<int> digitize(unsigned long n) 
{
    std::vector<int> ret;
    while (n != 0) {
        ret.push_back(std::labs(n % 10));
        n /= 10;
    }
    return ret;
}