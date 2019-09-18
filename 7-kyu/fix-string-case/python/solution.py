#include <algorithm>
#include <cctype>
#include <string>
#include <utility>

std::pair<int, int> count_cases(const std::string& str)
{
    int lower = 0, upper = 0;
    for (const char &c : str) {
        if (std::isupper(c)) upper++;
        else if (std::islower(c)) lower++;
    }
    return { upper, lower };
}

std::string solve(const std::string& str)
{
    auto case_counts = count_cases(str);
    auto str_cpy = str;
    if (case_counts.first > case_counts.second) { // upper > lower
        std::transform(str_cpy.begin(), str_cpy.end(), str_cpy.begin(), ::toupper);
    }
    else { // upper < lower || upper == lower
        std::transform(str_cpy.begin(), str_cpy.end(), str_cpy.begin(), ::tolower);
    }
    return str_cpy;
}