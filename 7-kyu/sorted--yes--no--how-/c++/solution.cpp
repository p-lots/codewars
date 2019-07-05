#include <algorithm>

std::string is_sorted_and_how(std::vector<int> array)
{
    std::vector<int> vec = array;
    std::sort(vec.begin(), vec.end());
    if (vec == array) return "yes, ascending";
    std::reverse(vec.begin(), vec.end());
    if (vec == array) return "yes, descending";
    return "no";
}