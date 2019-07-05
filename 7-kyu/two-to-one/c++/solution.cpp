#include <algorithm>
#include <string>

class TwoToOne
{
public:
    static std::string longest(const std::string &s1, const std::string &s2);
};

void add_letters(const std::string &from, std::string &to)
{
    for (const char &c : from) {
        if (to.find(c) == std::string::npos) {
            to += c;
        }
    }
}

std::string TwoToOne::longest(const std::string &s1, const std::string &s2)
{
    std::string ret = "";
    add_letters(s1, ret);
    add_letters(s2, ret);
    std::sort(ret.begin(), ret.end());
    return ret;
}