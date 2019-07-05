#include <numeric>
#include <string>

class Fracts
{

public:
    static unsigned long long gcd(unsigned long long a, unsigned long long b)
    {
        for (;;)
        {
            if (a == 0) return b;
            b %= a;
            if (b == 0) return a;
            a %= b;
        }
    }
    
    static unsigned long long lcm(unsigned long long a, unsigned long long b)
    {
        int temp = gcd(a, b);
    
        return temp ? (a / temp * b) : 0;
    }
    
    static std::string convertFrac(std::vector<std::vector<unsigned long long>> &lst)
    {
        unsigned long long l_c_m = 1;
        for (const auto vec : lst) {
            l_c_m = lcm(vec.back(), l_c_m);
        }
        std::string ret;
        for (const auto vec : lst) {
            unsigned long long multiplier = l_c_m / vec.back();
            ret += "(" + std::to_string(static_cast<unsigned long long>(vec.front()) * multiplier) + "," + std::to_string(l_c_m) + ")";
        }
        return ret;
    }
};
