#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> tokenize(const std::string &s)
{
    std::stringstream ss(s);
    std::string temp;
    std::vector<std::string> ret;
    while (std::getline(ss, temp, ' ')) ret.push_back(temp);
    return ret;
}

unsigned solve(const std::string &s, unsigned k)
{
    auto tokens = tokenize(s);
    unsigned ret = 0;
    for (unsigned i = 0; i < tokens.size(); i++) {
        for (unsigned j = 0; j < tokens.size(); j++) {
            if (i == j) continue;
            std::string concat = tokens[i] + tokens[j];
            int n = std::stoi(concat);
            if (n % k == 0) ret++;
        }
    }
    return ret;
}