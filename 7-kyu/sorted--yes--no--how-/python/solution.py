#include <algorithm>

std::string is_sorted_and_how(std::vector<int> array)
{
    std::vector<int> asc = array, desc = array;
    std::sort(asc.begin(), asc.end());
    std::sort(desc.rbegin(), desc.rend());
    if (asc == array) {
        return "yes, ascending";
    }
    else if (desc == array) {
        return "yes, descending";
    }
    return "no";
}