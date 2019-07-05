#include <algorithm>
#include <cctype>

std::string reverse_letter(const std::string &str)
{
    auto ret = str;
    ret.erase(std::remove_if(ret.begin(), ret.end(), [](char &c) { return !std::isalpha(c); }), ret.end());
    std::reverse(ret.begin(), ret.end());
    return ret;
}