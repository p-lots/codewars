#include <algorithm>
#include <cmath>
#include <string>

class RevRot
{
public:
    static std::string revRot(const std::string &strng, unsigned int sz);
    static bool sumCubesDivisByTwo(const std::string &n);
};

std::string RevRot::revRot(const std::string &strng, unsigned int sz)
{
    if ((sz <= 0 || strng.empty()) || sz > strng.length()) return "";
    std::string ret = "";
    for (unsigned i = 0; i < strng.length(); i += sz) {
        std::string chunk = strng.substr(i, sz);
        if (chunk.length() < sz) break;
        if (sumCubesDivisByTwo(chunk)) std::reverse(chunk.begin(), chunk.end());
        else std::rotate(chunk.begin(), chunk.begin() + 1, chunk.end());
        ret += chunk;
    }
    return ret;
}

bool RevRot::sumCubesDivisByTwo(const std::string &n)
{
    unsigned long long sum = 0ULL;
    for (const char c : n) {
        int digit = c - '0';
        sum += std::pow(digit, 3);
    }
    return sum % 2ULL == 0ULL;
}