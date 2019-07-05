#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

class LongestConsec
{
public:
    static std::string longestConsec(std::vector<std::string> &strarr, int k);
};

std::string LongestConsec::longestConsec(std::vector<std::string> &strarr, int k)
{
    if (strarr.empty() || strarr.size() < k || k <= 0) return "";
    else if (strarr.size() == k) return std::accumulate(strarr.begin(), strarr.end(), std::string(""));
    else if (k == 1) {
        return *std::max_element(strarr.begin(), strarr.end(),
            [](const std::string &lhs, const std::string &rhs) {
                return lhs.length() < rhs.length();
            });
    }
    std::vector<std::string> strings;
    for (auto it = strarr.begin(); it != strarr.end(); it++) {
        auto start = *it;
        for (auto inner_it = it + 1; std::abs(std::distance(it, inner_it)) < k /* inner_it != it + k */ && inner_it != strarr.end(); inner_it++) {
            start += *inner_it;
        }
        strings.push_back(start);
    }
    return *std::max_element(strings.begin(), strings.end(),
        [](const std::string &lhs, const std::string &rhs) {
            return lhs.length() < rhs.length();
        });
}