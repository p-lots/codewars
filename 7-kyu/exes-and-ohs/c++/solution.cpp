#include <algorithm>
#include <cctype>

bool XO(const std::string& str)
{
    auto str_cpy = str;
    std::transform(str_cpy.begin(), str_cpy.end(), str_cpy.begin(), ::tolower);
    return std::count(str_cpy.begin(), str_cpy.end(), 'o') == std::count(str_cpy.begin(), str_cpy.end(), 'x');
}