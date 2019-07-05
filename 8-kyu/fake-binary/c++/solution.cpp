#include <algorithm>
#include <string>

std::string fakeBin(std::string str)
{
    std::transform(str.begin(), str.end(), str.begin(), [](char c) {
        return c < (5 + '0') ? '0' : '1';
    });
    return str;
}