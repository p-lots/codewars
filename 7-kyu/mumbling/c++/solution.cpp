#include <cctype>

class Accumul
{
public:
    static std::string accum(const std::string &s);
};

std::string Accumul::accum(const std::string &s)
{
    std::string ret = "";
    unsigned i = 0;
    for (auto it = s.begin(); it != s.end(); it++) {
        char c = std::toupper(*it);
        ret += c;
        c = std::tolower(c);
        ret.append(i++, c);
        ret += "-";
    }
    ret.pop_back();
    return ret;
}