#include <string>
#include <vector>

class LongestConsec
{
public:
    static std::string longestConsec(std::vector<std::string> &strarr, int k);
};

std::string LongestConsec::longestConsec(std::vector<std::string> &strarr, int k)
{
    if ((strarr.size() == 0 || k > strarr.size()) || k <= 0) return "";
    std::vector<std::string> results;
    for (auto iter = strarr.begin(); iter != strarr.end(); iter++) {
        std::string pb = *iter;
        for (auto iter_2 = iter + 1; std::abs(std::distance(iter, iter_2)) < k && iter_2 != strarr.end(); iter_2++) {
            pb += *iter_2;
        }
        results.push_back(pb);
    }
    return *(std::max_element(results.begin(), results.end(),
        [](const std::string &lhs, const std::string &rhs) {
            return lhs.length() < rhs.length();
        }
    ));
}