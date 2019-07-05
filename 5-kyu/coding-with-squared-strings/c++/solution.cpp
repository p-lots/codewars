#include <algorithm>
#include <cmath>
#include <iterator>
#include <string>

class CodeSqStrings
{
public:
    static std::string code(const std::string &strng);
    static std::string decode(const std::string &strng);
};


std::string CodeSqStrings::code(const std::string &strng)
{
    int n = 1;
    std::string ret = strng;
    while (n * n < ret.length())
        n++;
    ret += std::string(n * n - ret.length(), '\v');
    std::string copy_from = ret;
    unsigned k = 0;
    for (unsigned i = 0; i < n; i++) {
        int m = n - 1;
        for (unsigned j = 0; j < n; j++) {
            ret[i * n + j] = copy_from[m * n + k];
            m--;
        }
        k++;
    }
    for (unsigned i = 1; i <= n; i++)
        ret.insert(i * n + i - 1, 1, '\n');
    ret.pop_back();
    return ret;
}

std::string CodeSqStrings::decode(const std::string &strng)
{
    std::string copy_from = strng;
    copy_from.erase(std::remove(copy_from.begin(), copy_from.end(), '\n'), copy_from.end());
    std::string ret = copy_from;
    int n = std::floor(std::sqrt(ret.length()));
    int m = n - 1;
    for (unsigned i = 0; i < n; i++) {
        unsigned k = 0;
        for (unsigned j = 0; j < n; j++) {
            ret[i * n + j] = copy_from[k * n + m];
            k++;
        }
        m--;
    }
    ret.erase(std::remove(ret.begin(), ret.end(), '\v'), ret.end());
    return ret;
}