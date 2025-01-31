#include <algorithm>
#include <cctype>
#include <numeric>

bool is_valid(std::string str)
{
    bool only_letters = true;
    for (const auto ch : str) {
        if (!std::isalpha(ch)) {
            only_letters = false;
        }
    }
    return !str.empty() && only_letters;
}

int sum_func(const char &lhs, const char &rhs)
{
    return static_cast<int>(std::toupper(lhs)) + static_cast<int>(std::toupper(rhs));
}

bool compare(std::string s1, std::string s2)
{
    int s1_sum = (is_valid(s1)
        ? std::accumulate(s1.begin(), s1.end(), 0, sum_func)
        : 0);
    int s2_sum = (is_valid(s2)
        ? std::accumulate(s2.begin(), s2.end(), 0, sum_func)
        : 0);
    
    return s1_sum == s2_sum;
}