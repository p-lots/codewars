#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

int find_short(std::string str)
{
    std::vector<std::string> str_split;
    std::stringstream ss(str);
    std::string temp;
    while (std::getline(ss, temp, ' ')) str_split.push_back(temp);
    auto min_it = std::min_element(str_split.begin(), str_split.end(),
        [](const std::string &lhs, const std::string &rhs) {
            return lhs.length() < rhs.length(); });
    return min_it->length();
}