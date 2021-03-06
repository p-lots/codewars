#include <algorithm>

std::vector<int> testit(std::vector<int> a, std::vector<int> b)
{
    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());
    a.erase(std::unique(a.begin(), a.end()), a.end());
    b.erase(std::unique(b.begin(), b.end()), b.end());
    a.insert(a.end(), b.begin(), b.end());
    std::sort(a.begin(), a.end());
    return a;
}