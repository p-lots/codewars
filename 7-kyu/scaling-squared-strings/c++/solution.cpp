#include <sstream>
#include <string>

class ScalingSqStrings
{
public:
    static std::vector<std::string> tokenize(const std::string &line)
    {
        std::stringstream ss(line);
        std::string temp;
        std::vector<std::string> ret;
        while (std::getline(ss, temp)) {
            ret.push_back(temp);
        }
        return ret;
    }
    static std::string scale(const std::string &strng, int k, int n)
    {
        if (strng.empty()) return "";
        auto tokens = tokenize(strng);
        std::string ret;
        for (auto it = tokens.begin(); it != tokens.end(); it++) {
            auto temp = *it;
            std::string line;
            for (unsigned i = 0; i < temp.length(); i++) {
                line += std::string(k, temp[i]);
            }
            for (unsigned i = 0; i < n; i++) {
                ret += line;
                if (!(it == tokens.end() - 1 && i == n - 1)) {
                    ret += '\n';
                }
            }
        }
        return ret;
    }
};