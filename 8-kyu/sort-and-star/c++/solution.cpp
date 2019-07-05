#include <algorithm>
#include <numeric>

std::string twoSort(std::vector<std::string> s)
{
    std::sort(s.begin(), s.end());
    auto first = s.front();
    std::string ret = "";
    for (auto it = first.begin(); it != first.end(); it++) {
        ret += *it;
        if (it != first.end() - 1) ret += "***";
    }
    return ret;
}