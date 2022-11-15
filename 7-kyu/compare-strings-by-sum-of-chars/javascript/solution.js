#include <algorithm>
#include <cctype>
#include <iostream>
#include <numeric>

int get_sum(std::string str)
{
    if (str.empty()) return 0;
    else if (!(std::all_of(str.begin(), str.end(), ::isalpha))) return 0;
    int ret = 0;
    for (char c : str) {
        ret += static_cast<int>(std::toupper(c));
    }
    return ret;
}

bool compare(std::string s1, std::string s2)
{
    bool ret = get_sum(s1) == get_sum(s2);
    std::cout << "s1: " << s1 << "\ts2: " << s2 << "\tret: " << (ret ? "True" : "False") << '\n';
    return ret;
}
