#include <algorithm>
#include <cctype>
#include <string>

std::string makeUpperCase (const std::string& input_str)
{
    std::string ret = input_str;
    std::transform(ret.begin(), ret.end(), ret.begin(), [](char &c) { return std::toupper(c); });
    return ret;
}