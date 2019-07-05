#include <cctype>

std::string capitalize(std::string s, std::vector<int> idxs)
{
    for (int i : idxs) {
        if (i > s.length()) continue;
        s[i] = std::toupper(s[i]);
    }
    return s;
}