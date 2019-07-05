#include <cmath>

int longest_palindrome(const std::string &s)
{
    if (s.length() < 2) return s.length();
    int ret = 1;
    for (unsigned i = 0; i < s.length() - 1; i++) {
        for (unsigned j = i + 1; j < s.length(); j++) {
            auto str = s.substr(i, j - i + 1);
            auto str_cpy = std::string(str.crbegin(), str.crend());
            if (str == str_cpy) ret = std::max(static_cast<unsigned long>(ret), str.length());
        }
    }
    return ret;
}