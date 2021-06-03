#include <algorithm>
#include <cmath>

std::string dec2bin(int n)
{
    int degree = static_cast<int>(std::log2(n));
    int digit;
    std::string ret = "";
    while (n > 0) {
        digit = n / std::pow(2, degree);
        ret += static_cast<char>(digit + '0');
        n -= std::pow(2, degree) * digit;
        if (degree > 0 && n == 0) {
            while (degree-- > 0) {
              ret += '0';
            }
            break;
        }
        degree--;
    }
    return ret;
}

std::string evil(int n)
{
    auto bin = dec2bin(n);
    return std::count(bin.begin(), bin.end(), '1') % 2 == 0 ? "It's Evil!" : "It's Odious!";
}