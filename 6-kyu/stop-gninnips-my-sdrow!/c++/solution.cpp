#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> tokenize(const std::string &str)
{
    std::vector<std::string> ret;
    std::stringstream ss(str);
    std::string temp;
    while (std::getline(ss, temp, ' ')) ret.push_back(temp);
    return ret;
}

std::string transformFunc(const std::string &str)
{
    if (str.length() >= 5) {
        std::string ret(str.crbegin(), str.crend());
        return ret;
    }
    else return str;
}

std::string spinWords(const std::string &str)
{
    auto tokens = tokenize(str);
    std::transform(tokens.begin(), tokens.end(), tokens.begin(), transformFunc);
    std::string ret = "";
    for (auto it = tokens.cbegin(); it != tokens.cend(); it++) {
        ret += *it;
        if (it != tokens.cend() - 1) ret += " ";
    }
    return ret;
}