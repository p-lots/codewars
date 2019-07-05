#include <cctype>

std::vector<std::string> wave(std::string y)
{
    std::vector<std::string> ret;
    if (y.empty()) return ret;
    for (unsigned i = 0; i < y.length(); i++) {
        if (!std::isalpha(y[i])) continue;
        std::string temp;
        if (i == 0) {
            temp += std::toupper(y[i]);
            temp += y.substr(i + 1);
            ret.push_back(temp);
        }
        else if (i < y.length() - 1) {
            temp += y.substr(0, i);
            temp += std::toupper(y[i]);
            temp += y.substr(i + 1);
            ret.push_back(temp);
        }
        else {
            temp += y.substr(0, i);
            temp += std::toupper(y[i]);
            ret.push_back(temp);
        }
    }
    return ret;
}