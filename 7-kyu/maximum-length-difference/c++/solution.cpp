#include <algorithm>
#include <cmath>

class MaxDiffLength
{
public:
    static int mxdiflg(std::vector<std::string> &a1, std::vector<std::string> &a2);
};

bool len_cmp(const std::string &lhs, const std::string &rhs)
{
    return lhs.length() < rhs.length();
}

int MaxDiffLength::mxdiflg(std::vector<std::string> &a1, std::vector<std::string> &a2)
{
    if (a1.empty() || a2.empty()) return -1;
    auto max_a1 = std::max_element(a1.begin(), a1.end(), len_cmp);
    auto min_a1 = std::min_element(a1.begin(), a1.end(), len_cmp);
    auto max_a2 = std::max_element(a2.begin(), a2.end(), len_cmp);
    auto min_a2 = std::min_element(a2.begin(), a2.end(), len_cmp);
    return std::max(std::abs((int)max_a1->length() - (int)min_a2->length()),
        std::abs((int)max_a2->length() - (int)min_a1->length()));
}