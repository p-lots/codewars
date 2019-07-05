#include <algorithm>

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
    std::sort(a1.begin(), a1.end(), len_cmp);
    std::sort(a2.begin(), a2.end(), len_cmp);
    auto a1_max = a1.rbegin();
    auto a1_min = a1.begin();
    auto a2_max = a2.rbegin();
    auto a2_min = a2.begin();
    auto l1 = a1_max->length() - a2_min->length();
    auto l2 = a2_max->length() - a1_min->length();
    return l1 > l2 ? l1 : l2;
}