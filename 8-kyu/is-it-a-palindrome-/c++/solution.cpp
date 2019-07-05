#include <algorithm>
#include <string>

std::string makeLower(const std::string &str)
{
    auto str_cpy = str;
    for (char &c : str_cpy) {
        if (std::isalpha(c)) c = std::isupper(c) ? std::tolower(c) : c;
    }
    return str_cpy;
}

bool isPalindrom (const std::string& str)
{
    auto lower_str = makeLower(str);
    return std::equal(lower_str.begin(), lower_str.end(), lower_str.rbegin());
}