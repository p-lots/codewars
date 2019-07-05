#include <algorithm>

std::vector<int> vectorize(int n)
{
    std::vector<int> ret;
    while (n > 0) {
        ret.push_back(n % 10);
        n /= 10;
    }
    std::reverse(ret.begin(), ret.end());
    return ret;
}

std::vector<int> digits(int n)
{
    std::vector<int> digits = vectorize(n);
    std::vector<int> ret;
    for (unsigned i = 0; i < digits.size(); i++) {
        for (unsigned j = i + 1; j < digits.size(); j++) {
            ret.push_back(digits[i] + digits[j]);
        }
    }
    return ret;
}