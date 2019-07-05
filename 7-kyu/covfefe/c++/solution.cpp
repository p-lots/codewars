#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> tokenize(std::string line)
{
    std::vector<std::string> ret;
    std::stringstream ss(line);
    std::string temp;
    while (std::getline(ss, temp, ' '))
        ret.push_back(temp);
    return ret;
}

std::string covfefe(std::string s)
{
    auto tokens = tokenize(s);
    std::string ret = "";
    bool found_coverage = false;
    for (auto it = tokens.begin(); it != tokens.end(); it++) {
        if (*it == "coverage") {
            ret += "covfefe";
            found_coverage = true;
        }
        else ret += *it;
        if (it != tokens.end() - 1) ret += " ";
    }
    if (s.back() == ' ') ret += " ";
    if (!found_coverage) ret += " covfefe";
    return ret;
}