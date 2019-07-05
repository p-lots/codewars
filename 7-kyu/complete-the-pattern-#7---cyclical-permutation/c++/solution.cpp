#include <string>

std::string pattern(int n)
{
    std::string ret = "";
    if (n < 1) return ret;
    if (n == 1) return "1";
    for (unsigned i = 1; i <= n; i++) {
        std::string to_append = "";
        for (unsigned j = i; j <= n; j++) to_append += std::to_string(j);
        for (unsigned j = 1; j < i; j++) to_append += std::to_string(j);
        ret += to_append + "\n";
    }
    ret.pop_back();
    return ret;
}