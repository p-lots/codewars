#include <cmath>

int string_to_number(const std::string& s) {
    bool neg = false;
    if (s[0] == '-') neg = true;
    int ten_mult = s.length() - (neg ? 2 : 1);
    int ret = 0;
    for (unsigned i = neg ? 1 : 0; i < s.length(); i++) {
        ret += (s[i] - '0') * std::pow(10, ten_mult);
        ten_mult--;
    }
    return neg ? -ret : ret;
}