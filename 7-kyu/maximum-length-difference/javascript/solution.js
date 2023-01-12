#include <algorithm>
#include <cmath>

class MaxDiffLength
{
public:
    static bool len_cmp(const std::string &lhs, const std::string &rhs) { return lhs.length() < rhs.length(); }
    static int mxdiflg(std::vector<std::string> &a1, std::vector<std::string> &a2)
    {
        if (a1.empty() || a2.empty()) return -1;
        std::sort(a1.begin(), a1.end(), len_cmp);
        std::sort(a2.begin(), a2.end(), len_cmp);
        int a1_f_len = a1.front().length(), a1_b_len = a1.back().length(), a2_f_len = a2.front().length(), a2_b_len = a2.back().length();
        return std::max(std::abs(a1_f_len - a2_b_len), std::abs(a2_f_len - a1_b_len));
    }
};
