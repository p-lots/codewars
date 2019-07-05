#include <algorithm>
#include <numeric>

int value(std::string str)
{
    if (str.empty()) return 0;
    else if (std::any_of(str.begin(), str.end(),
        [](const char &c) { return !std::isalpha(c); })) {
        return 0;
    }
    int ret = 0;
    for (const char c : str) {
        ret += std::toupper(c);
    }
    return ret;
}

bool compare(std::string s1, std::string s2)
{
    return value(s1) == value(s2);
}