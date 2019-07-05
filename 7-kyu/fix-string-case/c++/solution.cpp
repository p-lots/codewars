#include <algorithm>
#include <cctype>
#include <string>
#include <utility>

std::string solve(const std::string& str)
{
    auto upper_count = std::count_if(str.cbegin(), str.cend(), ::isupper);
    auto lower_count = std::count_if(str.cbegin(), str.cend(), ::islower);
    auto str_cpy = str;
    if (upper_count > lower_count) {
        std::transform(str_cpy.begin(), str_cpy.end(), str_cpy.begin(), ::toupper);
    }
    else { // upper < lower || upper == lower
        std::transform(str_cpy.begin(), str_cpy.end(), str_cpy.begin(), ::tolower);
    }
    return str_cpy;
}