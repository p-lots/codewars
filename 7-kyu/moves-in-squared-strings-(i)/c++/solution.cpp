#include <algorithm>
#include <functional>
#include <sstream>
#include <string>
#include <vector>

class Opstrings
{
public:
    static std::string vertMirror(const std::string &strng);
	  static std::string horMirror(const std::string &strng);
    static std::string oper(std::function<std::string(const std::string&)> f, const std::string &s);
private:
    static std::vector<std::string> tokenize(const std::string &s);
};

std::string Opstrings::oper(std::function<std::string(const std::string&)> f, const std::string &s)
{
    return f(s);
}

std::string Opstrings::horMirror(const std::string &strng)
{
    auto tokens = tokenize(strng);
    std::reverse(tokens.begin(), tokens.end());
    std::string ret = "";
    for (auto it = tokens.cbegin(); it != tokens.cend(); it++) {
        ret += *it;
        if (it != tokens.cend() - 1) ret += '\n';
    }
    return ret;
}

std::string Opstrings::vertMirror(const std::string &strng)
{
    auto tokens = tokenize(strng);
    std::string ret = "";
    for (auto it = tokens.cbegin(); it != tokens.cend(); it++) {
        auto s = *it;
        std::reverse(s.begin(), s.end());
        ret += s;
        if (it != tokens.cend() - 1) ret += '\n';
    }
    return ret;
}

std::vector<std::string> Opstrings::tokenize(const std::string &s)
{
    std::vector<std::string> ret;
    std::stringstream ss(s);
    std::string temp;
    while (std::getline(ss, temp, '\n')) ret.push_back(temp);
    return ret;
}